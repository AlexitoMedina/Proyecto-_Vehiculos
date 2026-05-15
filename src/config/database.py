from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import Generator
from src.config.settings import ADMIN_URL

class DatabaseConnector:
    def __init__(self, db_url: str):
        # Inicializa el motor de SQLAlchemy
        self._engine = create_engine(db_url, echo=True)
        
        # Configura la fábrica de sesiones
        self._session_factory = sessionmaker(
            autocommit=False, 
            autoflush=False, 
            bind=self._engine
        )

    def get_engine(self):
        """Devuelve el motor de la base de datos (Usado para crear tablas)"""
        return self._engine

    def get_db_session(self) -> Generator[Session, None, None]:
        """
        Dependency Provider para FastAPI.
        Crea una sesión de base de datos por cada petición HTTP
        y garantiza que se cierre al terminar.
        """
        session = self._session_factory()
        try:
            yield session
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()


db_manager = DatabaseConnector(ADMIN_URL)

