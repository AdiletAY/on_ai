import uuid

from datetime import datetime, timezone

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger, Identity, DateTime, UUID


class AuditMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )


class UUIDPrimaryKeyMixin:
    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
    )


class BigIntPrimaryKeyMixin:
    id: Mapped[int] = mapped_column(
        BigInteger,
        Identity(),
        primary_key=True,
    )


class IntPrimaryKeyMixin:
    id: Mapped[int] = mapped_column(primary_key=True)
