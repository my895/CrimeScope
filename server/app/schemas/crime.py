from p ydantic import BaseModel

class CrimeSchema(BaseModel):
    id: int
    description: str
    date: str

    class Config:
        orm_mode = True
