from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

def create_all_tables(engine):
    """Función dedicada a la creación de esquemas."""
    # Importamos los modelos aquí para evitar importaciones circulares
    from src.models.vehiculo_model import Vehiculo
    from src.models.conductor_model import Conductor
    Base.metadata.create_all(bind=engine)