from src.services.conductor_service import ConductorService
from src.schemas.conductor_schema import ConductorResponse, ConductorCreate

class ConductorController:
    def __init__(self, service_conductor = ConductorService):
        self.service_conductor = service_conductor

    def listar_conductores(self):
        return conductor_service.listar_conductores()

    def crear_conductor(self, conductor_body: ConductorCreate):
        datos_dict = conductor_body.model_dump()
        conductor = self.service_conductor.crear_conductor(datos_dict)
        return ConductorResponse.model_validate(conductor)