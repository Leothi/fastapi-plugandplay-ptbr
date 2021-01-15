from fastapi import APIRouter, Query
from loguru import logger

from api.models.exemplo import GetExampleResponse, PostExampleResponse, PostExampleInput
from api.modules import exemplo as modulo_exemplo

router = APIRouter()


@router.get('/exemplo_get', response_model=GetExampleResponse, summary="Sumário 1 - String upper case")
def router_get(string: str = Query(..., description="Retorna string de entrada em upper case", example="string")) -> float:
    """Rota de exemplo GET"""
    
    logger.log('LOG ROTA', "Chamada rota /exemplo_get")
    return {"exemplo_out": modulo_exemplo.string_upper(string)}

@router.post('/exemplo_post', response_model=PostExampleResponse, summary="Sumário 1 - String upper case")
def router_post(body: PostExampleInput) -> float:
    """Rota de exemplo POST"""
    
    logger.log('LOG ROTA', "Chamada rota /exemplo_get")
    return {"exemplo_out": modulo_exemplo.string_upper(**body.dict()['string'])}
