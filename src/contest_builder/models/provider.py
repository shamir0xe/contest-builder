from dataclasses import dataclass, field
from pylib_0xe.data.data_transfer_object import DataTransferObject


@dataclass
class Provider(DataTransferObject):
    """
    Represents a provider.
    """

    name: str
    abbreviations: list[str] = field(default_factory=list)

    @staticmethod
    def name_mapper(name: str) -> str:
        """
        Mapper function for provider name.
        """
        return name.lower()

    @staticmethod
    def abbreviations_mapper(abbr_list: list[str]) -> list[str]:
        """
        Mapper function for provider abbreviations.
        """
        return [abbr.lower() for abbr in abbr_list]
