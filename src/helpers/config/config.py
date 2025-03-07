from pylib_0xe.config.config import Config as CFG
from typing import Any


class Config:
    @staticmethod
    def read(selector: str, **kwargs) -> Any:
        return CFG.read(selector, base_path=__file__)
