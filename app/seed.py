from sqlalchemy.orm import Session
from datetime import date
from app.database import SessionLocal, engine
from app import models
from app.auth import gerar_hash_senha  


models.Base.metadata.create_all(bind=engine)


db: Session = SessionLocal()


administradores = [
    models.Administrador(
        nome="Ana Silva", 
        email="ana@gmail.com", 
        senha=gerar_hash_senha("senha123")
    ),
    models.Administrador(
        nome="Carlos Souza", 
        email="carlos@gmail.com", 
        senha=gerar_hash_senha("senha456")
    )
]


parques = [
    models.Parque(nome="Parque Nacional da Serra", localizacao="Rio de Janeiro", descricao="Parque com trilhas e biodiversidade incrível."),
    models.Parque(nome="Parque das Águas", localizacao="Minas Gerais", descricao="Parque com cachoeiras e trilhas leves.")
]


trilhas = [
    models.Trilha(nome="Trilha do Mirante", dificuldade="Média", distancia=5),
    models.Trilha(nome="Trilha das Cachoeiras", dificuldade="Fácil", distancia=3)
]


eventos = [
    models.Evento(nome="Caminhada Ecológica", data=date(2025, 7, 10), descricao="Promove a conscientização ambiental."),
    models.Evento(nome="Limpeza do Parque", data=date(2025, 8, 5), descricao="Mutirão de limpeza das trilhas.")
]


biodiversidades = [
    models.Biodiversidade(especie="Onça-pintada", tipo="Fauna", descricao="Mamífero carnívoro de grande porte."),
    models.Biodiversidade(especie="Ipê-amarelo", tipo="Flora", descricao="Árvore típica com flores amarelas.")
]

try:
    db.add_all(administradores)
    db.add_all(parques)
    db.add_all(trilhas)
    db.add_all(eventos)
    db.add_all(biodiversidades)

    db.commit()
    print("Dados inseridos com sucesso!")

except Exception as e:
    print(f"Erro ao inserir dados: {e}")
    db.rollback()

finally:
    db.close()
