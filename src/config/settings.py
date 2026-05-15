import os
from dotenv import load_dotenv

# Carga las variables del archivo .env
load_dotenv()

# Usamos los nombres exactos de tu .env
PORT = os.getenv("PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD") # Actualizado
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Armamos las URLs usando f-strings
ADMIN_URL = f"postgresql+pg8000://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/postgres"
APP_DB_URL = f"postgresql+pg8000://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"