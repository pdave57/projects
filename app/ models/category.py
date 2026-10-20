from sqlalchemy import (
    Column, 
    Date, 
    DateTime, 
    ForeignKey, 
    Integer, 
    Numeric, 
    String,
)
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(
        Integer, 
        primary_key=True, 
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(50), nullable=False, unique=True
    )

    type: Mapped[str] = mapped_column(
        String(255), nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )