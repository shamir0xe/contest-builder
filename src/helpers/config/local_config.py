from typing import Any
import os
from src.helpers.config.config import Config
from pylib_0xe.file.file import File
from pylib_0xe.json.json_helper import JsonHelper


class LocalConfig:
    def __init__(
        self,
        filename: str,
    ) -> None:
        found = False
        try:
            while not found:
                found = True
                try:
                    self.json = File.read_json(f"{filename}.json")
                except Exception:
                    filename = os.path.join("..", filename)
                    found = False
        except Exception:
            raise Exception(
                "Please provide a local config file by running \
                'contest-builder --init' command"
            )

    def get(self, selector: str = "", default: Any = None) -> Any:
        value = JsonHelper.selector_get_value(self.json, selector)
        if value != {}:
            return value
        return default

    @staticmethod
    def read(selector: str) -> Any:
        filename = Config.read("main.config.local")
        return LocalConfig(filename).get(selector)
