from __future__ import annotations
import os
from dataclasses import dataclass, field
from src.helpers.model.finders.language_finder import LanguageFinder
from src.helpers.model.finders.provider_finder import ProviderFinder
from src.helpers.model.problem_helper import ProblemHelper
from src.models.provider import Provider
from src.models.language import Language
from libs.pylib.data.data_transfer_object import DataTransferObject


@dataclass
class Problem(DataTransferObject):
    name: str = ""
    verdict: str = ""
    problem_set: str = ""
    provider: Provider = field(default_factory=ProviderFinder.default)
    language: Language = field(default_factory=LanguageFinder.default)
    path: str = "."

    def name_mapper(self, name: str) -> str:
        return ProblemHelper.problem_name_mapper(name)

    def provider_mapper(self, provider: str) -> Provider:
        # set provider name
        return ProviderFinder.by_abbreviation(provider)

    def language_mapper(self, language: str) -> Language:
        # set the language
        return LanguageFinder.by_abbreviation(language)

    @staticmethod
    def modifiables() -> list[str]:
        return ["name", "provider", "language"]

    @property
    def full_name(self) -> str:
        return os.path.join(self.path, f"{self.name}.{self.language.ext}")

    @property
    def full_input_name(self) -> str:
        return os.path.join(self.path, f"{self.name}.in")
    
    def __str__(self) -> str:
        return self.full_name
