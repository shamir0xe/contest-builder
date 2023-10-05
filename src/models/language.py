from __future__ import annotations
from dataclasses import dataclass
from libs.pylib.data.data_transfer_object import DataTransferObject


@dataclass
class Language(DataTransferObject):
    name: str = ""
    extensions: list[str] = []

    def name_mapper(self, name: str) -> str:
        return name.lower()

    def extensions_mapper(self, ext_list: list[str]) -> list[str]:
        return list(map(lambda ext: ext.lower(), ext_list))

