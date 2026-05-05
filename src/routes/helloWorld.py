from fastapi import APIRouter
from src.controllers import helloWorld 

router = APIRouter(prefix="/helloWorld", tags=["Hello World"])

@router.get("/")
def get_hello_world():
    return helloWorld.greetings()