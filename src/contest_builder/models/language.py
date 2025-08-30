from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from pylib_0xe.data.data_transfer_object import DataTransferObject


@dataclass
class Language(DataTransferObject):
    """Represents a programming language."""

    name: str = ""
    abbreviations: List[str] = field(default_factory=list)
    extensions: List[str] = field(default_factory=list)

    @staticmethod
    def name_mapper(name: str) -> str:
        """Map the language name to lowercase."""
        return name.lower()

    @staticmethod
    def extensions_mapper(ext_list: List[str]) -> List[str]:
        """Map each extension to lowercase."""
        return [ext.lower() for ext in ext_list]

    @property
    def ext(self) -> str:
        """Get the first extension in lowercase."""
        return self.extensions[0].lower() if self.extensions else ""

    @ext.setter
    def ext(self, value: str) -> None:
        """Set the first extension to the specified value."""
        if value in self.extensions:
            while self.extensions[0] != value:
                self.extensions = [*self.extensions[1:], self.extensions[0]]

    def __eq__(self, other: object) -> bool:
        """Check if two Language objects are equal."""
        if not isinstance(other, Language):
            return False
        return self.name == other.name
