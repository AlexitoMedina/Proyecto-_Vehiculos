from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.schemas.vehiculo_schema import VehiculoCreate, VehiculoUpdate
from src.services import vehiculo_service


def listar_vehiculos(db: Session):
    return vehiculo_service.obtener_vehiculos(db)


def buscar_vehiculo(id: int, db: Session):
    vehiculo = vehiculo_service.obtener_vehiculo_por_id(db, id)

    if not vehiculo:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")

    return vehiculo


def buscar_por_placa(placa: str, db: Session):
    vehiculo = vehiculo_service.obtener_vehiculo_por_placa(db, placa)

    if not vehiculo:
        raise HTTPException(status_code=404, detail="Placa no autorizada")

    return vehiculo


def registrar_vehiculo(vehiculo: VehiculoCreate, db: Session):
    existe = vehiculo_service.obtener_vehiculo_por_placa(db, vehiculo.placa)

    if existe:
        raise HTTPException(status_code=400, detail="La placa ya está registrada")

    return vehiculo_service.crear_vehiculo(db, vehiculo)


def editar_vehiculo(id: int, datos: VehiculoUpdate, db: Session):
    vehiculo = vehiculo_service.actualizar_vehiculo(db, id, datos)

    if not vehiculo:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")

    return vehiculo


def borrar_vehiculo(id: int, db: Session):
    vehiculo = vehiculo_service.eliminar_vehiculo(db, id)

    if not vehiculo:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")

    return {"mensaje": "Vehículo eliminado correctamente"}