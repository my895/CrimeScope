from fastapi import FastAPI
from app.routes import crime

app = FastAPI()

app.include_router(crime.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to CrimeXplore API"}
