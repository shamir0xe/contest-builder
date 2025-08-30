import re
from ...types.name_types import NameTypes


class ProblemHelper:
    @staticmethod
    def problem_name_mapper(name: str) -> str:
        name = name.lower()
        name = re.sub(r"(\(|\)|\[|\])", " ", name)
        name = re.sub(r"(\.|\\|\/|\,|\:|\;|\'|\")", " ", name)
        name = re.sub(r"\s+", "-", name.strip())
        name = re.sub(r"\-+", "-", name)
        name = re.sub(r"div\-(\d+)", r"div\1", name)
        name = re.sub(r"\-(\+|\>|\<)\-", r"\1", name)
        return name

    @staticmethod
    def name_type_mapper(name: str) -> NameTypes:
        name = name.lower()
        for name_type in NameTypes:
            if name == name_type.name.lower()[: len(name)]:
                return name_type
        # defaults to ALPHABETICAL
        return NameTypes.ALPHABETICAL

    @staticmethod
    def create_problem_name(idx: int, name_type: NameTypes) -> str:
        if name_type is NameTypes.ALPHABETICAL:
            return chr(ord("a") + idx)
        elif name_type is NameTypes.NUMERICAL:
            return f"{idx + 1}"
        elif name_type is NameTypes.ROMAN:
            # TODO
            return ""
        return ""
