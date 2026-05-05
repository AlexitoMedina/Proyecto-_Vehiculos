from fastapi import FastAPI
from src.routes.helloWorld import router as helloWorld
#from starlette.exceptions import HTTPException
#from starlette.middleware.cors import CORSMiddleware



def get_application() -> FastAPI:
    
    application = FastAPI()

    application.include_router(helloWorld, prefix="/api")


    return application


app = get_application()