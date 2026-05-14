from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional


class VehiculoBase(BaseModel):
    placa: str
    marca: Optional[str] = None
    modelo: Optional[str] = None
    color: Optional[str] = None
    propietario: str
    tipo_vehiculo: Optional[str] = None
    estado: Optional[str] = "autorizado"


class VehiculoCreate(VehiculoBase):
    pass


class VehiculoUpdate(BaseModel):
    placa: Optional[str] = None
    marca: Optional[str] = None
    modelo: Optional[str] = None
    color: Optional[str] = None
    propietario: Optional[str] = None
    tipo_vehiculo: Optional[str] = None
    estado: Optional[str] = None


class VehiculoResponse(VehiculoBase):
    id: int
    fecha_registro: datetime

    model_config = ConfigDict(from_attributes=True)