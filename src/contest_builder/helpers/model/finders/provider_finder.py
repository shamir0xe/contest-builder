from ....helpers.config.local_config import LocalConfig
from ....models.provider import Provider


class ProviderFinder:
    @staticmethod
    def by_name(name: str) -> Provider:
        filtered = ProviderFinder.filter_providers(
            lambda provider: name == provider.name
        )
        return ProviderFinder.get_single_provider(filtered, name)

    @staticmethod
    def by_abbreviation(abbreviation: str) -> Provider:
        filtered = ProviderFinder.filter_providers(
            lambda provider: abbreviation in provider.abbreviations
        )
        return ProviderFinder.get_single_provider(filtered, abbreviation)

    @staticmethod
    def all() -> list[Provider]:
        providers = LocalConfig.read("providers")
        return [
            Provider.from_dict({"name": provider, **properties})
            for provider, properties in providers.items()
        ]

    @staticmethod
    def default() -> Provider:
        problem_provider = LocalConfig.read("problem.provider")
        return ProviderFinder.by_abbreviation(problem_provider)

    @staticmethod
    def filter_providers(predicate) -> list[Provider]:
        return list(filter(predicate, ProviderFinder.all()))

    @staticmethod
    def get_single_provider(filtered: list[Provider], search_criteria: str) -> Provider:
        if not filtered:
            raise Exception(f"No valid provider found by {search_criteria}")
        return filtered[0]
