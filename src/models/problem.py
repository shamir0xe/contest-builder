from __future__ import annotations
import os
from dataclasses import dataclass
from src.actions.problem_name_mapper import problem_name_mapper
from src.types.languages import Languages
from src.types.providers import Providers
from src.actions.provider_finder import provider_finder
from src.actions.language_finder import language_finder
from src.actions.extension_mapper import extension_mapper
from libs.pylib.data.data_transfer_object import DataTransferObject


@dataclass
class Problem(DataTransferObject):
    name: str = ""
    verdict: str = ""
    provider: Providers = Providers.CODEFORCES
    language: Languages = Languages.CPP
    problem_set: str = ""
    path: str = "."

    def name_mapper(self, name: str) -> str:
        return problem_name_mapper(name)

    def provider_mapper(self, provider: str) -> Providers:
        # set provider name
        return provider_finder(provider)

    def language_mapper(self, language: str) -> Languages:
        # set the language
        return language_finder(language)

    @property
    def full_name(self) -> str:
        extension = extension_mapper(self.language)
        return os.path.join(self.path, f"{self.name}.{extension}")

    @property
    def full_input_name(self) -> str:
        return os.path.join(self.path, f"{self.name}.in")
