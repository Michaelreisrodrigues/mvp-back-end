from pydantic import BaseModel, EmailStr

# Base comum para criação
class AdministradorBase(BaseModel):
    nome: str
    email: EmailStr

# Schema de criação (entrada de dados)
class AdministradorCreate(AdministradorBase):
    senha: str

# Schema de resposta (sem senha!)
class Administrador(AdministradorBase):
    id: int

    model_config = {
        "from_attributes": True
    }
