from __future__ import annotations
import os
from typing import Any
from dataclasses import dataclass, field
from ...helpers.config.config import Config
from pylib_0xe.file.file import File
from pylib_0xe.json.json_helper import JsonHelper


@dataclass
class LocalConfig:
    filename: str
    home_path: list[str] = field(
        default_factory=lambda: [os.path.normpath(os.path.abspath(os.sep))]
    )

    def build(
        self,
    ) -> LocalConfig:
        found = False
        path = os.getcwd()
        try:
            while not found:
                if path in self.home_path:
                    raise Exception
                found = True
                try:
                    self.json = File.read_json(f"{self.filename}.json")
                except Exception:
                    self.filename = os.path.join("..", self.filename)
                    path = os.path.normpath(os.path.join(path, ".."))
                    found = False
        except Exception:
            print(
                "Please provide a local config file by running\
                'contest-builder --init' command"
            )
            exit(0)
        return self

    def get(self, selector: str = "", default: Any = None) -> Any:
        value = JsonHelper.selector_get_value(self.json, selector)
        if value != {}:
            return value
        return default

    @staticmethod
    def read(selector: str) -> Any:
        filename = Config.read("main.config.local")
        return LocalConfig(filename).build().get(selector)
