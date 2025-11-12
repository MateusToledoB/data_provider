from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db
from passlib.context import CryptContext

router = APIRouter(prefix="/contacts", tags=["Contatos"])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    try:
        return pwd_context.verify(plain_password, hashed_password)
    except Exception:
        return False

@router.post("/get_contact", response_model=schemas.ContactResponse)
def get_contact(request: schemas.ContactRequest, db: Session = Depends(get_db)):
    
    user = db.query(models.User).filter(models.User.name == request.name).first()

   
    if not user or not verify_password(request.password, user.password):
        raise HTTPException(status_code=401, detail="Usuário ou senha inválidos")

    
    contact = db.query(models.Numero).filter(models.Numero.cpf == request.cpf).first()

    if not contact:
        raise HTTPException(status_code=404, detail="CPF não encontrado")

    return contact
