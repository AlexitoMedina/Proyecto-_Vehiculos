import uvicorn
from src.config.settings import PORT

if __name__ == "__main__":
    print(f"Iniciando servidor principal en el puerto {PORT}...")
    uvicorn.run(
        "src.server:app",
        host="0.0.0.0", 
        port=int(PORT), 
        reload=True 
    )