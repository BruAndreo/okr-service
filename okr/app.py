from fastapi import FastAPI
from .docs import title, description
from .resources.routes import objectives, singin, authentication

app = FastAPI(title=title, description=description)

@app.get("/")
def echo():
    return { "message": "Hello to OKR Service" }

app.include_router(singin.router)
app.include_router(authentication.router)
app.include_router(objectives.router)

@app.on_event("startup")
def on_startup():
    print("OKR Service online")

@app.on_event("shutdown")
def on_shutdown():
    print("OKR Service shutdown")