from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from typing import Union

from model import Base


class Navio(Base):
    __tablename__ = 'navio'

    id = Column("pk_navio", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    imo = Column(Integer)
    eta = Column(String(8))
    etb = Column(String(8))
    ets = Column(String(8))
    terminal = Column(String(30))
    obs = Column(String(400))
    email = Column(String(300))
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, nome: str, imo: Integer, eta: str, etb: str, ets: str, terminal: str, obs: str, email: str,
                 data_insercao: Union[DateTime, None] = None):
        """
        Cria um cadastro de navio

        Arguments:
            nome: nome do navio.
            imo: numero que identifica o navio
            eta: data estimada de chegada
            etb: data estimada de atracacao
            ets: data estimada de desatracacao
            terminal: terminal de operacao
            obs: observacoes da operacao
            email: email dos clientes
            data_insercao: data de quando o produto foi inserido à base
        """
        self.nome = nome
        self.imo = imo
        self.eta = eta
        self.etb = etb
        self.ets = ets
        self.terminal = terminal
        self.obs = obs
        self.email = email

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao
