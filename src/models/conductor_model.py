# -*- coding: utf-8 -*-
import uuid
from sqlalchemy import String, Uuid, Integer
from sqlalchemy.orm import Mapped, mapped_column
from src.models.base import Base

class Conductor(Base):
    __tablename__ = "conductores"

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid, 
        primary_key=True, 
        default=uuid.uuid4
    )
    
    
    ci: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    nombre: Mapped[str] = mapped_column(String(50), nullable=False)
    apellido: Mapped[str] = mapped_column(String(50), nullable=False)
    ru: Mapped[int] = mapped_column(Integer, unique=True, nullable=True)
    
    def __repr__(self) -> str:
        return (
            f"Conductor(id={self.id!r}, ci={self.ci!r}, "
            f"nombre={self.nombre!r}, apellido={self.apellido!r}, "
            f"ru={self.ru!r})"
        )