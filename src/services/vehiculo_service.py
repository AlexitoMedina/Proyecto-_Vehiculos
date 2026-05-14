from sqlalchemy.orm import Session
from src.models.vehiculo_model import Vehiculo
from src.schemas.vehiculo_schema import VehiculoCreate, VehiculoUpdate


def obtener_vehiculos(db: Session):
    return db.query(Vehiculo).all()


def obtener_vehiculo_por_id(db: Session, vehiculo_id: int):
    return db.query(Vehiculo).filter(Vehiculo.id == vehiculo_id).first()


def obtener_vehiculo_por_placa(db: Session, placa: str):
    return db.query(Vehiculo).filter(Vehiculo.placa == placa).first()


def crear_vehiculo(db: Session, vehiculo: VehiculoCreate):
    nuevo_vehiculo = Vehiculo(**vehiculo.model_dump())

    db.add(nuevo_vehiculo)
    db.commit()
    db.refresh(nuevo_vehiculo)

    return nuevo_vehiculo


def actualizar_vehiculo(db: Session, vehiculo_id: int, datos: VehiculoUpdate):
    vehiculo = obtener_vehiculo_por_id(db, vehiculo_id)

    if not vehiculo:
        return None

    datos_actualizados = datos.model_dump(exclude_unset=True)

    for campo, valor in datos_actualizados.items():
        setattr(vehiculo, campo, valor)

    db.commit()
    db.refresh(vehiculo)

    return vehiculo


def eliminar_vehiculo(db: Session, vehiculo_id: int):
    vehiculo = obtener_vehiculo_por_id(db, vehiculo_id)

    if not vehiculo:
        return None

    db.delete(vehiculo)
    db.commit()

    return vehiculo