from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="ATS Resume Generator")

@app.get("/")
def health_check():
    return {"status": "ok"}

app.include_router(router, prefix="/api")
