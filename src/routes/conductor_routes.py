from fastapi import APIRouter, Depends
from src.controllers.conductor_controller import ConductorController
from src.config.container import get_conductor_controller
from src.schemas.conductor_schema import ConductorCreate

router = APIRouter(
    prefix="/conductores",
    tags=["Conductores"]
)

@router.post("/")
def crear_conductores(
    conductor_body: ConductorCreate,
    controller: ConductorController = Depends(get_conductor_controller)
    ):
    return controller.crear_conductor(conductor_body)