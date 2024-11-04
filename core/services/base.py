from uuid import UUID
from typing import Generic, TypeVar, Sequence, Optional

from core.schemas.base import BaseSchema as _BaseSchema
from core.repositories.base import BaseRepository as _BaseRepository


_ModelType = TypeVar("_ModelType")
_RepositoryType = TypeVar("_RepositoryType", bound=_BaseRepository)
_CreateSchemaType = TypeVar("_CreateSchemaType", bound=_BaseSchema)
_UpdateSchemaType = TypeVar("_UpdateSchemaType", bound=_BaseSchema)


class BaseServiceUUID(
    Generic[
        _ModelType,
        _RepositoryType,
        _CreateSchemaType,
        _UpdateSchemaType,
    ]
):
    def __init__(self, repository: _RepositoryType) -> None:
        self.repository = repository

    async def create(self, data: _CreateSchemaType) -> _ModelType:
        """Creates a new entity"""
        return await self.repository.create(data)

    async def update(self, id: UUID, data: _UpdateSchemaType) -> Optional[_ModelType]:
        """
        Updates an entity by ID

        """

        return await self.repository.update(data, id=id)

    async def delete(self, id: UUID) -> None:
        """
        Deletes an entity by ID

        """
        await self.repository.delete(id=id)

    async def get(self, **filters) -> Optional[_ModelType]:
        """
        Retrieves a single entity by filters

        """
        return await self.repository.get(**filters)

    async def list(self, **filters) -> Sequence[_ModelType]:
        """
        Retrieves multiple entities by filters.

        """
        return await self.repository.list(**filters)


class BaseServiceInt(
    Generic[
        _ModelType,
        _RepositoryType,
        _CreateSchemaType,
        _UpdateSchemaType,
    ]
):
    def __init__(self, repository: _RepositoryType) -> None:
        self.repository = repository

    async def create(self, data: _CreateSchemaType) -> _ModelType:
        """Creates a new entity"""
        return await self.repository.create(data)

    async def update(self, id: int, data: _UpdateSchemaType) -> Optional[_ModelType]:
        """
        Updates an entity by ID

        """

        return await self.repository.update(data, id=id)

    async def delete(self, id: int) -> None:
        """
        Deletes an entity by ID

        """
        await self.repository.delete(id=id)

    async def get(self, **filters) -> Optional[_ModelType]:
        """
        Retrieves a single entity by filters

        """
        return await self.repository.get(**filters)

    async def list(self, **filters) -> Sequence[_ModelType]:
        """
        Retrieves multiple entities by filters.

        """
        return await self.repository.list(**filters)
