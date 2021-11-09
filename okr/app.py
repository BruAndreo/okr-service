from fastapi import FastAPI
from .docs import title, description

app = FastAPI(title=title, description=description)

@app.get("/")
def echo():
    return { "message": "Hello to OKR Service" }

@app.on_event("startup")
def on_startup():
    print("OKR Service online")

@app.on_event("shutdown")
def on_shutdown():
    print("OKR Service shutdown")