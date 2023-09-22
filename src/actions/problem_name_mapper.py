import re


def problem_name_mapper(name: str) -> str:
    name = name.lower()
    name = re.sub(r"(\(|\)|\[|\])", " ", name)
    name = re.sub(r"(\.|\\|\/|\,|\:|\;|\'|\")", " ", name)
    name = re.sub(r"\s+", "-", name.strip())
    name = re.sub(r"\-+", "-", name)
    name = re.sub(r"div\-(\d+)", r"div\1", name)
    name = re.sub(r"\-(\+|\>|\<)\-", r"\1", name)
    return name
