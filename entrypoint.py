import uvicorn
from okr.app import app
from okr.config import settings

if __name__ == "__main__":
    uvicorn.run(
        "entrypoint:app", 
        port=settings.app.port, 
        log_level=settings.app.log_level)