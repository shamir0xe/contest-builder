from dataclasses import dataclass, field
from src.helpers.model.finders.language_finder import LanguageFinder
from src.helpers.model.finders.provider_finder import ProviderFinder
from src.helpers.model.problem_helper import ProblemHelper
from src.models.language import Language
from src.models.provider import Provider
from src.types.name_types import NameTypes
from libs.pylib.data.data_transfer_object import DataTransferObject


@dataclass
class Contest(DataTransferObject):
    name_type: NameTypes = NameTypes.ALPHABETICAL
    name: str = ""
    problem_cnt: int = 0
    provider: Provider = field(default_factory=ProviderFinder.default)
    language: Language = field(default_factory=LanguageFinder.default)
    path: str = "."

    @staticmethod
    def modifiables() -> list[str]:
        return ["name", "provider", "language", "problem_cnt", "name_type"]

    def problem_cnt_mapper(self, number: int | str) -> int:
        return int(number)

    def name_type_mapper(self, key: str) -> NameTypes:
        return ProblemHelper.name_type_mapper(key)

    def name_mapper(self, name: str) -> str:
        return ProblemHelper.problem_name_mapper(name)

    def provider_mapper(self, provider: str) -> Provider:
        # set provider name
        return ProviderFinder.by_abbreviation(provider)

    def language_mapper(self, language: str) -> Language:
        # set the language
        return LanguageFinder.by_abbreviation(language)
