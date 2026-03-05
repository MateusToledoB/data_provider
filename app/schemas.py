from pydantic import BaseModel, ConfigDict


class AuthData(BaseModel):
    name: str
    password: str


class ContactRequest(AuthData):
    cpf: str


class ContactResponse(BaseModel):
    cpf: str
    numero: str | None = None
    email: str | None = None

    model_config = ConfigDict(from_attributes=True)
