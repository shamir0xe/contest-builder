from dataclasses import dataclass
from src.actions.name_type_mapper import name_type_mapper
from libs.pylib.data.data_transfer_object import DataTransferObject
from src.types.name_types import NameTypes


@dataclass
class Contest(DataTransferObject):
    name_type: NameTypes = NameTypes.ALPHABETICAL
    name: str = ""
    site: str = ""
    template_path: str = ""
    problem_cnt: int = 0

    def name_type_mapper(self, key: str) -> NameTypes:
        return name_type_mapper(key)

    def name_mapper(self, name: str) -> str:
        return name.lower()
