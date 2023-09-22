from typing import Any
from libs.pylib.file.file import File
from libs.pylib.json.json_helper import JsonHelper


class LocalConfig:
    def __init__(
        self,
        filename: str,
    ) -> None:
        self.json = File.read_json(f"{filename}.json")

    def get(self, selector: str = "", default: Any = None) -> Any:
        value = JsonHelper.selector_get_value(self.json, selector)
        if value != {}:
            return value
        return default

    @staticmethod
    def read(selector: str) -> Any:
        index = selector.find(".")
        if index < 0:
            return LocalConfig(selector).get()
        filename = selector[:index]
        selector = selector[index + 1 :]
        return LocalConfig(filename).get(selector)
