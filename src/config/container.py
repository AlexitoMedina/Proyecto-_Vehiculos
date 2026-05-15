from fastapi import Depends
from sqlalchemy.orm import Session

# Importación de la Base de Datos
from src.config.database import db_manager

# Importaciones del módulo Vehículo
from src.repository.conductor_repository import ConductorRepository
from src.services.conductor_service import ConductorService
from src.controllers.conductor_controller import ConductorController

# --- DEPENDENCIAS BASE ---
def get_db():
    """Provee la conexión a la base de datos."""
    yield from db_manager.get_db_session()


# --- DEPENDENCIAS DE VEHÍCULOS ---
def get_conductor_repository(db: Session = Depends(get_db)) -> ConductorRepository:
    """Construye el Repositorio inyectando la DB."""
    return ConductorRepository(db)

def get_conductor_service(repo: ConductorRepository = Depends(get_conductor_repository)) -> ConductorService:
    """Construye el Servicio inyectando el Repositorio."""
    return ConductorService(repo)

def get_conductor_controller(service: ConductorService = Depends(get_conductor_service)) -> ConductorController:
    """Construye el Controlador inyectando el Servicio."""
    return ConductorController(service)

# Si mañana creas el módulo "Conductores", agregarías sus inyectores aquí abajo.