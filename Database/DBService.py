from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Base para nossos modelos

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    presenca = Column(Integer)
    faltas = Column(Integer)
    porcentagem = Column(Integer)
    telefone = Column(String)



# Conectar ao banco
engine = create_engine('sqlite:///BancoUsuarios.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

'''
# Criar novo usuário
novo_usuario = Usuario(nome="Aline Sebastiana Melissa Barbosa", presenca = 0 ,faltas = 0,  porcentagem = 100, telefone = "51993492356")

# Adicionar à sessão
session.add(novo_usuario)

# Salvar no banco
session.commit()

# Fechar sessão
session.close()
'''

def nome_alunos():
    session = Session()
    try:
        nomes = [aluno.nome for aluno in session.query(Usuario).all()]
        return nomes
    finally:
        session.close()
    

def marcar_falta(nome):
    session = Session()
    usuario = session.query(Usuario).filter(Usuario.nome == nome).first()
    if usuario:
# Atualizar dados
        usuario.faltas = Usuario.faltas + 1
        session.commit()
        print("Usuário atualizado!")
    else:
        print("Usuário não encontrado")

    session.close()

def marcar_presenca(nome):
    session = Session()
    usuario = session.query(Usuario).filter(Usuario.nome == nome).first()
    if usuario:
# Atualizar dados
        usuario.presenca = Usuario.presenca + 1
        session.commit()
        print("Usuário atualizado!")
    else:
        print("Usuário não encontrado")

    session.close()

def calcular_porcentagem(nome):
    session = Session()
    usuario = session.query(Usuario).filter(Usuario.nome == nome).first()
    if usuario:
        if usuario.presenca + usuario.faltas > 0:
            porcentagem = (usuario.presenca / (usuario.presenca + usuario.faltas)) * 100
            usuario.porcentagem = porcentagem
            session.commit()
            print(f"Porcentagem de presença de {nome}: {porcentagem:.2f}%")
        else:
            print(f"{nome} não possui registros de presença ou falta.")
    else:
        print("Usuário não encontrado")

    session.close()

def verificar_porcentagem(nome):
    session = Session()
    usuario = session.query(Usuario).filter(Usuario.nome == nome).first()
    if usuario:
        if usuario.porcentagem < 70:
            print(usuario.telefone, " - Alerta: Presença abaixo de 70%!", usuario.nome)
    else:
        print("Usuário não encontrado")
        return None

    session.close()

def adicionar_aluno(nome, telefone):
    session = Session()
    novo_usuario = Usuario(nome=nome, presenca=0, faltas=0, porcentagem=0, telefone=telefone)
    session.commit()
    session.close()


def remover_aluno(nome):
    session = Session()
    usuario = session.query(Usuario).filter(Usuario.nome == nome).first()
    if usuario:
        session.delete(usuario)
        session.commit()
        print(f"Usuário {nome} removido com sucesso!")
    else:
        print("Usuário não encontrado")

    session.close()

def atualizar_numero(nome, novo_numero):
    session = Session()
    usuario = session.query(Usuario).filter(Usuario.nome == nome).first()
    if usuario:
        usuario.telefone = novo_numero
        session.commit()
        print(f"Número de telefone de {nome} atualizado para {novo_numero}.")
    else:
        print("Usuário não encontrado")

    session.close()

def listar_por_presenca():
    session = Session()
    usuarios = session.query(Usuario).order_by(Usuario.porcentagem.desc()).all()
    for usuario in usuarios:
        print(f"{usuario.nome} - Presença: {usuario.porcentagem:.2f}%")
    session.close()