from typing import List

from pydantic import BaseModel


class Size(BaseModel):
    height: int = 0
    width: int = 0


class ResizeParams(BaseModel):
    sizes: List[Size]
