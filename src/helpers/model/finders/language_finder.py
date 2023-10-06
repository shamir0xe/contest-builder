from src.helpers.config.local_config import LocalConfig
from src.models.language import Language


class LanguageFinder:
    @staticmethod
    def by_name(name: str) -> Language:
        return list(
            filter(lambda language: name == language.name, LanguageFinder.all())
        )[0]

    @staticmethod
    def by_abbreviation(abbreviation: str) -> Language:
        return list(
            filter(
                lambda language: abbreviation in language.abbreviations,
                LanguageFinder.all(),
            )
        )[0]

    @staticmethod
    def all() -> list[Language]:
        res = []
        languages = LocalConfig.read("languages")
        for language, properties in languages.items():
            res.append(Language(name=language).from_dict(properties))
        return res

    @staticmethod
    def default() -> Language:
        return LanguageFinder.by_name(LocalConfig.read("problem.language"))
