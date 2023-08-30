from src.types.name_types import NameTypes


def name_type_mapper(name: str) -> NameTypes:
    name = name.lower()
    for name_type in NameTypes:
        if name == name_type.name.lower()[: len(name)]:
            return name_type
    # defaults to ALPHABETICAL
    return NameTypes.ALPHABETICAL
