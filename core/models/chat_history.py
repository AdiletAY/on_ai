from sqlalchemy.orm import Mapped, mapped_column

from core.models.base import Base
from core.models.mixins import IntPrimaryKeyMixin


class ChatHistoryModel(IntPrimaryKeyMixin, Base):
    # простоты ради, сохраню только эти поля
    message: Mapped[str] = mapped_column()
    created: Mapped[int] = mapped_column()

    def __repr__(self):
        return f"ChatHistoryModel<{self.id}>"
