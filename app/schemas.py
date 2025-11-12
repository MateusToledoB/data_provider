from pydantic import BaseModel

class AuthData(BaseModel):
    name: str
    password: str

class ContactRequest(AuthData):
    cpf: str

class ContactResponse(BaseModel):
    cpf: str
    numero: str | None = None
    email: str | None = None

    class Config:
        orm_mode = True

