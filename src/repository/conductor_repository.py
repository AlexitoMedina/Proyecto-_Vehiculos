from sqlalchemy.orm import Session
from src.models.conductor_model import Conductor

class ConductorRepository:
   
    def __init__(self, db: Session):
        self.db = db
        
    def create(self, conductor: Conductor) -> Conductor:
        self.db.add(conductor)
        self.db.commit()
        self.db.refresh(conductor)
        return conductor
        