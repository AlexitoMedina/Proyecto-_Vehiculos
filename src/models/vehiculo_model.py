from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from src.database.base import Base


class Vehiculo(Base):
    __tablename__ = "vehiculos"

    id = Column(Integer, primary_key=True, index=True)
    placa = Column(String(20), unique=True, index=True, nullable=False)
    marca = Column(String(50), nullable=True)
    modelo = Column(String(50), nullable=True)
    color = Column(String(30), nullable=True)
    propietario = Column(String(100), nullable=False)
    tipo_vehiculo = Column(String(50), nullable=True)
   
    estado = Column(String(20), default="autorizado")
    fecha_registro = Column(DateTime, default=datetime.utcnow)