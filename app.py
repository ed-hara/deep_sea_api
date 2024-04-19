
from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError
from model import Session, Navio
from logger import logger
from schemas import *
from flask_cors import CORS


info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação",
               description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
navio_tag = Tag(
    name="Navio", description="Adição, visualização e remoção de navios à base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/navio', tags=[navio_tag],
          responses={"200": NavioViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_navio(form: NavioSchema):
    """Adiciona um novo Navio à base de dados

    Retorna uma representação dos navios associados.
    """
    navio = Navio(
        nome=form.nome,
        imo=form.imo,
        eta=form.eta,
        etb=form.etb,
        ets=form.ets,
        terminal=form.terminal,
        obs=form.obs,
        email=form.email)
    logger.debug(f"Adicionando navio de nome: '{navio.nome}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando produto
        session.add(navio)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado navio de nome: '{navio.nome}'")
        return apresenta_navio(navio), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Navio de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar navio '{navio.nome}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar navio '{navio.nome}', {error_msg}")
        return {"mesage": error_msg}, 400


@app.get('/navios', tags=[navio_tag],
         responses={"200": ListagemNaviosSchema, "404": ErrorSchema})
def get_navios():
    """Faz a busca por todos os Navios cadastrados

    Retorna uma representação da listagem de navios.
    """
    logger.debug(f"Coletando navios ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    navios = session.query(Navio).all()

    if not navios:
        # se não há navios cadastrados
        return {"navios": []}, 200
    else:
        logger.debug(f"%d navios econtrados" % len(navios))
        # retorna a representação de navios
        print(navios)
        return apresenta_navios(navios), 200


@app.get('/navio', tags=[navio_tag],
         responses={"200": NavioViewSchema, "404": ErrorSchema})
def get_navio(query: NavioBuscaSchema):
    """Faz a busca por um Navio a partir do id do navio

    Retorna uma representação dos navios associados.
    """
    navio_id = query.id
    logger.debug(f"Coletando dados sobre navio #{navio_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    navio = session.query(Navio).filter(Navio.id == navio_id).first()

    if not navio:
        # se o navio não foi encontrado
        error_msg = "Navio não encontrado na base :/"
        logger.warning(f"Erro ao buscar navio '{navio_id}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Navio econtrado: '{navio.nome}'")
        # retorna a representação de navio
        return apresenta_navio(navio), 200


@app.delete('/navio', tags=[navio_tag],
            responses={"200": NavioDelSchema, "404": ErrorSchema})
def del_navio(query: NavioBuscaNomeSchema):
    """Deleta um Navio a partir do nome do navio informado

    Retorna uma mensagem de confirmação da remoção.
    """
    navio_nome = unquote(unquote(query.nome))
    print(navio_nome)
    logger.debug(f"Deletando dados sobre navio #{navio_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Navio).filter(Navio.nome == navio_nome).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado navio #{navio_nome}")
        return {"mesage": "Navio removido", "nome": navio_nome}
    else:
        # se o navio não foi encontrado
        error_msg = "Navio não encontrado na base :/"
        logger.warning(f"Erro ao deletar navio #'{navio_nome}', {error_msg}")
        return {"mesage": error_msg}, 404
