from __future__ import annotations
from dataclasses import dataclass, field
from libs.pylib.data.data_transfer_object import DataTransferObject


@dataclass
class Provider(DataTransferObject):
    name: str = ""
    abbreviations: list[str] = field(default_factory=list)

    def name_mapper(self, name: str) -> str:
        return name.lower()

    def abbreviations_mapper(self, abbr_list: list[str]) -> list[str]:
        return list(map(lambda abbr: abbr.lower(), abbr_list))
