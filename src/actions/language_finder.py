from src.types.languages import Languages


def language_finder(name: str) -> Languages:
    name = name.lower()
    if name == "cpp" or name == "c++" or name == "seepp":
        return Languages.CPP
    if name == "py" or name.count("python") >= 1:
        return Languages.PYTHON
    return Languages.TXT
