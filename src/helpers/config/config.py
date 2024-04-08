from pylib_0xe.config.config import Config as CFG
from typing import Any


class Config(CFG):
    @staticmethod
    def read(selector: str, **kwargs) -> Any:
        config = CFG(file_path=__file__)
        return config.read(selector, **kwargs)
