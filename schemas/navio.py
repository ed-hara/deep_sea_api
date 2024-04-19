from pydantic import BaseModel
from typing import Optional, List
from model.navio import Navio
from datetime import datetime


class NavioSchema(BaseModel):
    """ Define como um novo Navio a ser inserido deve ser representado
    """
    nome: str = "Long May"
    imo: int = 9847085
    eta: str = "2024-06-10"
    etb: str = "2024-06-12"
    ets: str = "2024-06-14"
    terminal: str = "CPBS"
    obs: str = "Necessária renovação do certificado de ship sanitation"
    email: str = "edu.hara@gmail.com, edu.hara10@gmail.com"


class NavioBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no id do navio.
    """
    id: int = 1


class NavioBuscaNomeSchema(BaseModel):
    """ Busca do navio por Nome"""
    nome: str = "Long May"


class ListagemNaviosSchema(BaseModel):
    """ Define como uma listagem de navios será retornada.
    """
    navios: List[NavioSchema]


def apresenta_navios(navios: List[Navio]):
    """ Retorna uma representação do navio seguindo o schema definido em
        NavioViewSchema.
    """
    result = []
    for navio in navios:
        result.append({
            "nome": navio.nome,
            "imo": navio.imo,
            "eta": navio.eta,
            "etb": navio.etb,
            "ets": navio.ets,
            "terminal": navio.terminal,
            "obs": navio.obs,
            "email": navio.email
        })

    return {"navios": result}


class NavioViewSchema(BaseModel):
    """ Define como um cadastro de navio será retornado.
    """
    id: int = 1
    nome: str = "Long May"
    imo: int = 9847085
    eta: str = "2024-06-10"
    etb: str = "2024-06-12"
    ets: str = "2024-06-14"
    terminal: str = "CPBS"
    email: str = "edu.hara@gmail.com, edu.hara10@gmail.com"


class NavioDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """

    mesage: str
    nome: str


def apresenta_navio(navio: Navio):
    """ Retorna uma representação do navio seguindo o schema definido em
        NavioViewSchema.
    """
    return {
        "id": navio.id,
        "nome": navio.nome,
        "imo": navio.imo,
        "eta": navio.eta,
        "etb": navio.etb,
        "ets": navio.ets,
        "terminal": navio.terminal,
        "email": navio.email
    }
