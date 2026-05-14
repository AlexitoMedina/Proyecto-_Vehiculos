from fastapi import APIRouter, HTTPException
from typing import List
from datetime import datetime

from src.schemas.vehiculo_schema import VehiculoCreate, VehiculoUpdate, VehiculoResponse


router = APIRouter(
    prefix="/vehiculos",
    tags=["Vehículos"]
)

vehiculos = []
contador_id = 1


@router.get("/", response_model=List[VehiculoResponse])
def listar_vehiculos():
    return vehiculos


@router.post("/", response_model=VehiculoResponse)
def crear_vehiculo(vehiculo: VehiculoCreate):
    global contador_id

    placa = vehiculo.placa.upper().strip()

    for item in vehiculos:
        if item["placa"] == placa:
            raise HTTPException(status_code=400, detail="La placa ya está registrada")

    nuevo_vehiculo = vehiculo.model_dump()
    nuevo_vehiculo["id"] = contador_id
    nuevo_vehiculo["placa"] = placa
    nuevo_vehiculo["fecha_registro"] = datetime.utcnow()

    vehiculos.append(nuevo_vehiculo)
    contador_id += 1

    return nuevo_vehiculo


@router.get("/placa/{placa}", response_model=VehiculoResponse)
def buscar_por_placa(placa: str):
    placa = placa.upper().strip()

    for vehiculo in vehiculos:
        if vehiculo["placa"] == placa:
            return vehiculo

    raise HTTPException(status_code=404, detail="Vehículo no encontrado")


@router.get("/{id}", response_model=VehiculoResponse)
def buscar_vehiculo(id: int):
    for vehiculo in vehiculos:
        if vehiculo["id"] == id:
            return vehiculo

    raise HTTPException(status_code=404, detail="Vehículo no encontrado")


@router.put("/{id}", response_model=VehiculoResponse)
def actualizar_vehiculo(id: int, datos: VehiculoUpdate):
    for vehiculo in vehiculos:
        if vehiculo["id"] == id:
            datos_actualizados = datos.model_dump(exclude_unset=True)

            if "placa" in datos_actualizados:
                datos_actualizados["placa"] = datos_actualizados["placa"].upper().strip()

            vehiculo.update(datos_actualizados)
            return vehiculo

    raise HTTPException(status_code=404, detail="Vehículo no encontrado")


@router.delete("/{id}")
def eliminar_vehiculo(id: int):
    for index, vehiculo in enumerate(vehiculos):
        if vehiculo["id"] == id:
            vehiculos.pop(index)
            return {"mensaje": "Vehículo eliminado correctamente"}

    raise HTTPException(status_code=404, detail="Vehículo no encontrado")