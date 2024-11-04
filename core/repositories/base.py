from typing import Generic, TypeVar, Sequence, Type, Optional, List


from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy import select, update, delete, ColumnExpressionArgument

from core.models.base import Base as _Base
from core.schemas.base import BaseSchema as _BaseSchema

_ModelType = TypeVar("_ModelType", bound=_Base)
_CreateSchemaType = TypeVar("_CreateSchemaType", bound=_BaseSchema)
_UpdateSchemaType = TypeVar("_UpdateSchemaType", bound=_BaseSchema)


class BaseRepository(
    Generic[
        _ModelType,
        _CreateSchemaType,
        _UpdateSchemaType,
    ]
):
    def __init__(self, model: Type[_ModelType], session: AsyncSession) -> None:
        self.model = model
        self.session = session

    async def create(self, data: _CreateSchemaType) -> _ModelType:
        """
        Creates a new record.

        """
        instance = self.model(**data.model_dump())
        self.session.add(instance)
        try:
            await self.session.commit()
            await self.session.refresh(instance)
        except (IntegrityError, SQLAlchemyError) as e:
            await self.session.rollback()
            raise SQLAlchemyError(
                f"Failed to create {self.model.__name__}. Detail: {str(e)}"
            )
        return instance

    async def update(self, data: _UpdateSchemaType, **filters) -> Optional[_ModelType]:
        """
        Update a record with given filters.

        """

        statement = (
            update(self.model)
            .values(**data.model_dump(exclude_unset=True, exclude_none=True))
            .filter_by(**filters)
            .returning(self.model)
        )
        try:
            result: Result = await self.session.execute(statement)
            await self.session.commit()
            return result.scalar_one()
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise SQLAlchemyError(
                f"Failed to update {self.model.__name__}. Detail: {str(e)}"
            )

    async def delete(self, **filters) -> None:
        """
        Deletes a record based on filters.

        """

        statement = delete(self.model).filter_by(**filters)
        try:
            await self.session.execute(statement)
            await self.session.commit()
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise SQLAlchemyError(
                f"Failed to delete {self.model.__name__}. Detail: {str(e)}"
            )

    async def list(
        self,
        columns: Optional[List[ColumnExpressionArgument[_ModelType]]] = None,
        **filters,
    ) -> Sequence[_ModelType]:
        """
        Retrieves multiple records based on filters and selected columns.

        """
        statement = select(columns if columns else self.model)
        if filters:
            statement = statement.filter_by(**filters)
        result: Result = await self.session.execute(statement)
        return result.scalars().all()

    async def get(
        self,
        columns: Optional[List[ColumnExpressionArgument[_ModelType]]] = None,
        **filters,
    ) -> Optional[_ModelType]:
        """
        Retrieves a single record based on filters and selected columns.

        """
        statement = select(columns if columns else self.model).filter_by(**filters)
        result: Result = await self.session.execute(statement)
        return result.scalar_one_or_none()
