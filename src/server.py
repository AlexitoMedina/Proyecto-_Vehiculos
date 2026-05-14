from fastapi import FastAPI
from src.config.database import engine

from src.routes.helloWorld import router as helloWorld
from src.routes.vehiculo_routes import router as vehiculo_router


#from starlette.exceptions import HTTPException
#from starlette.middleware.cors import CORSMiddleware



def get_application() -> FastAPI:
    
    application = FastAPI()

    application.include_router(helloWorld, prefix="/api")
    application.include_router(vehiculo_router, prefix="/api")
    try:
        engine.connect()
        print("The databas is conected")
    except Exception as e:
        print ("Error:"+e)

    return application


app = get_application()