from humps import decamelize
from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, declared_attr

from core.config import settings


class Base(DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(naming_convention=settings.db.naming_convention)

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{decamelize(cls.__name__)}s"
