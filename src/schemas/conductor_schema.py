import uuid
from pydantic import BaseModel, ConfigDict


class ConductorCreate(BaseModel):
    ci: int
    nombre: str
    apellido: str
    ru: int
    
class ConductorResponse(BaseModel):
    id: uuid.UUID
    ci: int
    nombre: str
    apellido: str
    ru: int
    model_config = ConfigDict(from_attributes=True)