import os
import uvicorn

from src.server import app

if __name__ == "__main__":
    uvicorn.run(
        "src.server:app",
        host="0.0.0.0", 
        port=os.environ.get("PORT"), 
        reload=True 
    )