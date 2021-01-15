from fastapi import APIRouter, Query
from loguru import logger

from api.models.exemplo import GetExampleResponse, PostExampleResponse, PostExampleInput
from api.modules import exemplo as modulo_exemplo

router = APIRouter()


@router.get('/get', response_model=GetExampleResponse, summary="Sumário 1 - String upper case.")
def router_get(string: str = Query(..., description="String de entrada.", example="string")) -> dict:
    """Rota de exemplo GET. Retorna string em upper case."""

    logger.log('LOG ROTA', "Chamada rota /get")
    return {"exemplo_out": modulo_exemplo.string_upper(string)}


@router.post('/post', response_model=PostExampleResponse, summary="Sumário 2 - String upper case.")
def router_post(body: PostExampleInput) -> dict:
    """Rota de exemplo POST. Retorna string em upper case."""

    logger.log('LOG ROTA', "Chamada rota /post")
    return {"exemplo_out": modulo_exemplo.string_upper(body.dict()['string'])}
