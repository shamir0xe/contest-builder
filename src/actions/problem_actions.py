from src.types.name_types import NameTypes


def create_problem_name(idx: int, name_type: NameTypes) -> str:
    if name_type is NameTypes.ALPHABETICAL:
        return chr(ord("a") + idx)
    elif name_type is NameTypes.NUMERICAL:
        return f"{idx + 1}"
    elif name_type is NameTypes.ROMAN:
        # TODO
        return ""
    return ""
