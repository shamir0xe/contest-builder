from dataclasses import dataclass, field
from src.helpers.model.finders.language_finder import LanguageFinder
from src.helpers.model.finders.provider_finder import ProviderFinder
from src.helpers.model.problem_helper import ProblemHelper
from src.models.language import Language
from src.models.provider import Provider
from src.types.name_types import NameTypes
from pylib_0xe.data.data_transfer_object import DataTransferObject


@dataclass
class Contest(DataTransferObject):
    """
    Represents a contest.
    """

    name_type: NameTypes = NameTypes.ALPHABETICAL
    name: str = ""
    problem_cnt: int = 0
    provider: Provider = field(default_factory=ProviderFinder.default)
    language: Language = field(default_factory=LanguageFinder.default)
    path: str = "."

    @staticmethod
    def modifiables() -> list[str]:
        """
        Returns a list of modifiable attributes.
        """
        return ["name", "provider", "language", "problem_cnt", "name_type"]

    @staticmethod
    def problem_cnt_mapper(number: int | str) -> int:
        """
        Mapper function for problem count.
        """
        return int(number)

    @staticmethod
    def name_type_mapper(key: str) -> NameTypes:
        """
        Mapper function for name types.
        """
        return ProblemHelper.name_type_mapper(key)

    @staticmethod
    def name_mapper(name: str) -> str:
        """
        Mapper function for contest name.
        """
        return ProblemHelper.problem_name_mapper(name)

    @staticmethod
    def provider_mapper(provider: str) -> Provider:
        """
        Mapper function for contest provider.
        """
        print(f"getting provider mapper {provider}")
        return ProviderFinder.by_abbreviation(provider)

    @staticmethod
    def language_mapper(language: str) -> Language:
        """
        Mapper function for contest language.
        """
        return LanguageFinder.by_abbreviation(language)
