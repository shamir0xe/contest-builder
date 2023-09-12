from __future__ import annotations
from dataclasses import dataclass
import os
from libs.pylib.data.data_transfer_object import DataTransferObject
from src.types.languages import Languages


@dataclass
class Problem(DataTransferObject):
    name: str = ""
    verdict: str = ""
    language: Languages = Languages.CPP
    extension: str = ""
    path: str = "."

    @property
    def full_name(self) -> str:
        return os.path.join(self.path, f"{self.name}.{self.extension}")
    
    @property
    def full_input_name(self) -> str:
        return os.path.join(self.path, f"{self.name}.in")

