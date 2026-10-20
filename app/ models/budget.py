from datetime import datetime
from decimal import Decimal
from pyclbr import Class
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

class Budget(Base):
    __tablename__ = "budgets"

    id: Mapped[int] = mapped_column(
        Integer, 
        primary_key=True, 
        index=True
    )

    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id"), 
        nullable=False
    )

    category_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("categories.id"), 
        nullable=False
    )

    amount: Mapped[Decimal] = mapped_column(
        Numeric(10, 2), nullable=False
    )

    start_date: Mapped[date] = mapped_column(
        Date, nullable=False
    )

    end_date: Mapped[date] = mapped_column(
        Date, nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )