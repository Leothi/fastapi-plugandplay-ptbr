import os

from pydantic import BaseSettings
from api.utils.logger import DEFAULT_FORMAT


class EnvironmentVariables(BaseSettings):
    # FastAPI
    FASTAPI_HOST: str = '0.0.0.0'
    FASTAPI_PORT: int = 8080
    FASTAPI_RELOAD: bool = False
    FASTAPI_ACCESS_LOG: bool = False
    FASTAPI_ROOT_PATH: str = ""

    # Logger
    LOGGER_SWAGGER: bool = False
    LOGGER_IGNORE: str = '/docs /redoc /openapi.json /metrics /health /favicon.ico / /# /_static/perfil_ico.png /_static/perfil.png'
    LOGURU_FORMAT: str = DEFAULT_FORMAT
    LOG_LOCAL: bool = False
    LOG_LEVEL: int = 20

    # Development
    RUNNING_ENV: str


envs = EnvironmentVariables()

bind = os.environ.get('GUNICORN_BIND', '0.0.0.0:8080')
workers = os.environ.get('GUNICORN_WORKERS', '1')
reload = os.environ.get('GUNICORN_RELOAD', False)
loglevel = os.environ.get('GUNICORN_LOGLEVEL', 'info')
timeout = os.environ.get('GUNICORN_TIMEOUT', 30)
graceful_timeout = os.environ.get('GUNICORN_GRACEFUL_TIMEOUT', 30)
