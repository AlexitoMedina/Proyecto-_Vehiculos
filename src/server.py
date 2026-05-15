import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI

# 1. Importaciones de Configuración e Infraestructura
from src.config.settings import ADMIN_URL, DB_NAME
from src.config.database import db_manager
from src.config.db_setup import ensure_database_exists
from src.models.base import create_all_tables

# 2. Importaciones de Rutas (Asegúrate de que estas rutas existan en tus archivos)
from src.routes.helloWorld import router as helloWorld
from src.routes.vehiculo_routes import router as vehiculo_router
from src.routes.conductor_routes import router as conductor_router


# --- RESPONSABILIDAD 1: GESTIÓN DEL CICLO DE VIDA ---
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Esto se ejecuta ANTES de que el servidor empiece a recibir peticiones
    try:
        print("Verificando base de datos...")
        ensure_database_exists(ADMIN_URL, DB_NAME)
        
        print("Verificando tablas...")
        
        create_all_tables(db_manager.get_engine())
        
        print("Infraestructura y Base de datos listas.")
    except Exception as e:
        import traceback
        print(f"Error crítico en infraestructura:\n{traceback.format_exc()}")
    
    yield # Aquí FastAPI se queda escuchando peticiones
    
    # Esto se ejecuta al apagar el servidor
    print("Servidor apagado correctamente.")


# --- RESPONSABILIDAD 2: CONFIGURACIÓN DE FASTAPI ---
def get_application() -> FastAPI:
    application = FastAPI(
        title="API Sistema de Parqueo",
        lifespan=lifespan 
    )

    # Registramos tus endpoints
    application.include_router(helloWorld, prefix="/api")
    application.include_router(vehiculo_router, prefix="/api")
    application.include_router(conductor_router, prefix="/api")

    return application

app = get_application()