import os
from pathlib import Path

from pydantic import BaseSettings

root_dir = Path(__file__).parents[0]


class Settings(BaseSettings):
    debug: bool
    server_port: int = 8000
    server_host: str = '127.0.0.1'


settings = Settings(
    _env_file=os.path.join(root_dir, '../.env'),
    _env_file_encoding='utf-8'
)
