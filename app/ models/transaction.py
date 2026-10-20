from datetime import date, datetime
from decimal import Decimal

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

class Transaction(Base):
    __tablename__ = "transactions"

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

    type: Mapped[str] = mapped_column(
        String(10), nullable=False
    )

    description: Mapped[str] = mapped_column(
        String(255), nullable=True
    )
    
    transaction_date: Mapped[date] = mapped_column(
        Date, default=date.today, nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)