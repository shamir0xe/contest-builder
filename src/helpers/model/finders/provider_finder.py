from src.helpers.config.local_config import LocalConfig
from src.models.provider import Provider


class ProviderFinder:
    @staticmethod
    def by_name(name: str) -> Provider:
        return list(
            filter(lambda provider: name == provider.name, ProviderFinder.all())
        )[0]

    @staticmethod
    def by_abbreviation(abbreviation: str) -> Provider:
        return list(
            filter(
                lambda provider: abbreviation in provider.abbreviations,
                ProviderFinder.all(),
            )
        )[0]

    @staticmethod
    def all() -> list[Provider]:
        res = []
        providers = LocalConfig.read("providers")
        for provider, properties in providers.items():
            res.append(Provider(name=provider).from_dict(properties))
        return res

    @staticmethod
    def default() -> Provider:
        return ProviderFinder.by_name(LocalConfig.read("problem.provider"))
