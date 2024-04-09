from ....helpers.config.local_config import LocalConfig
from ....models.language import Language


class LanguageFinder:
    @staticmethod
    def by_name(name: str) -> Language:
        filtered = LanguageFinder.filter_languages(
            lambda language: name == language.name
        )
        return LanguageFinder.get_single_language(filtered, name)

    @staticmethod
    def by_abbreviation(abbreviation: str) -> Language:
        filtered = LanguageFinder.filter_languages(
            lambda language: abbreviation in language.abbreviations
        )
        return LanguageFinder.get_single_language(filtered, abbreviation)

    @staticmethod
    def all() -> list[Language]:
        languages = LocalConfig.read("languages")
        return [
            Language.from_dict({"name": language, **properties})
            for language, properties in languages.items()
        ]

    @staticmethod
    def default() -> Language:
        problem_language = LocalConfig.read("problem.language")
        return LanguageFinder.by_abbreviation(problem_language)

    @staticmethod
    def filter_languages(predicate) -> list[Language]:
        return list(filter(predicate, LanguageFinder.all()))

    @staticmethod
    def get_single_language(filtered: list[Language], search_criteria: str) -> Language:
        if not filtered:
            raise Exception(f"No valid language found by {search_criteria}")
        return filtered[0]
