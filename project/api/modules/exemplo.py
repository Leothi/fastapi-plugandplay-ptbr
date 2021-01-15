from loguru import logger

from fastapi.responses import JSONResponse


def string_upper(string: str) -> str:
    """Transforma a mensagem para upper case.

    :param string: string de entrada.
    :type string: str
    :return: string em upper case.
    :rtype: str
    """
    logger.info("Transformando mensagem para upper string")
    return string.upper()
