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


# Criar novo usuário
novo_usuario = Usuario(nome="Aline Sebastiana Melissa Barbosa", presenca = 0 ,faltas = 0,  porcentagem = 100, telefone = "51993492356")

# Adicionar à sessão
session.add(novo_usuario)

# Salvar no banco
session.commit()

# Fechar sessão
session.close()
