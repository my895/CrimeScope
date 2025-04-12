from fastapi import APIRouter
from app.models.crime import Crime
from app.schemas.crime import CrimeSchema
import pandas as pd

router = APIRouter()

@router.get("/api/crimes", response_model=list[CrimeSchema])
async def get_crimes():
    df = pd.read_csv('data/crimes.csv')
    return df.to_dict(orient='records')
