from dataclasses import dataclass, field
import os
from src.helpers.model.finders.language_finder import LanguageFinder
from src.helpers.model.finders.provider_finder import ProviderFinder
from src.helpers.model.problem_helper import ProblemHelper
from src.models.provider import Provider
from src.models.language import Language
from pylib_0xe.data.data_transfer_object import DataTransferObject


@dataclass
class Problem(DataTransferObject):
    """
    Represents a problem.
    """

    name: str = ""
    verdict: str = ""
    problem_set: str = ""
    provider: Provider = field(default_factory=ProviderFinder.default)
    language: Language = field(default_factory=LanguageFinder.default)
    path: str = "."

    def name_mapper(self, name: str) -> str:
        """
        Mapper function for problem name.
        """
        return ProblemHelper.problem_name_mapper(name)

    def provider_mapper(self, provider: str) -> Provider:
        """
        Mapper function for problem provider.
        """
        return ProviderFinder.by_abbreviation(provider)

    def language_mapper(self, language: str) -> Language:
        """
        Mapper function for problem language.
        """
        return LanguageFinder.by_abbreviation(language)

    @staticmethod
    def modifiables() -> list[str]:
        """
        Returns a list of modifiable attributes.
        """
        return ["name", "provider", "language"]

    @property
    def full_name(self) -> str:
        """
        Returns the full file name of the problem.
        """
        return os.path.join(self.path, f"{self.name}.{self.language.ext}")

    @property
    def full_input_name(self) -> str:
        """
        Returns the full file name of the input for the problem.
        """
        return os.path.join(self.path, f"{self.name}.in")

    def __str__(self) -> str:
        """
        Returns a string representation of the problem.
        """
        return self.full_name

