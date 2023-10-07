from __future__ import annotations
from dataclasses import dataclass, field
from libs.pylib.data.data_transfer_object import DataTransferObject


@dataclass
class Language(DataTransferObject):
    name: str = ""
    abbreviations: list[str] = field(default_factory=list)
    extensions: list[str] = field(default_factory=list)

    def name_mapper(self, name: str) -> str:
        return name.lower()

    def extensions_mapper(self, ext_list: list[str]) -> list[str]:
        return list(map(lambda ext: ext.lower(), ext_list))

    @property
    def ext(self) -> str:
        return self.extensions[0]

    @ext.setter
    def ext(self, value) -> None:
        while self.extensions[0] != value:
            self.extensions = [*self.extensions[1:], self.extensions[0]]

    def __eq__(self, __value: Language) -> bool:
        return self.name == __value.name
