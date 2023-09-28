from dataclasses import dataclass
from src.actions.language_finder import language_finder
from src.actions.provider_finder import provider_finder
from src.actions.name_type_mapper import name_type_mapper
from src.actions.problem_name_mapper import problem_name_mapper
from src.types.name_types import NameTypes
from src.types.languages import Languages
from src.types.providers import Providers
from libs.pylib.data.data_transfer_object import DataTransferObject


@dataclass
class Contest(DataTransferObject):
    name_type: NameTypes = NameTypes.ALPHABETICAL
    name: str = ""
    problem_cnt: int = 0
    provider: Providers = Providers.CODEFORCES
    language: Languages = Languages.CPP
    path: str = "."

    def problem_cnt_mapper(self, number: int | str) -> int:
        return int(number)

    def name_type_mapper(self, key: str) -> NameTypes:
        return name_type_mapper(key)

    def name_mapper(self, name: str) -> str:
        return problem_name_mapper(name)

    def provider_mapper(self, provider: str) -> Providers:
        # set provider name
        return provider_finder(provider)

    def language_mapper(self, language: str) -> Languages:
        # set the language
        return language_finder(language)
