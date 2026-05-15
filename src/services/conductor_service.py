from src.repository.conductor_repository import ConductorRepository
from src.models.conductor_model import Conductor


class ConductorService:
    def __init__ (self, conductor_repository = ConductorRepository):
        self.conductor_repository = conductor_repository
    
    def crear_conductor(self, datos_conductor = dict):
        nuevo_conductor = Conductor(**datos_conductor)
        conductor_creado = self.conductor_repository.create(nuevo_conductor)
        return conductor_creado