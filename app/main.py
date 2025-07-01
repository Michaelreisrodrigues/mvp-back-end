from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from .database import engine, Base
from app.routers import parque, evento, administrador, biodiversidade, trilha
from app.routers.login_router import router as login_router


app = FastAPI(title="API Tere Verde")


Base.metadata.create_all(bind=engine)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


app.include_router(login_router)  
app.include_router(parque.router)
app.include_router(trilha.router)
app.include_router(evento.router)
app.include_router(biodiversidade.router)
app.include_router(administrador.router)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API Tere Verde"}


@app.get("/token-test")
def token_test(token: str = Depends(oauth2_scheme)):
    return {"msg": "Token válido!", "token": token}
