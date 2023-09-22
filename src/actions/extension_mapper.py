from src.types.languages import Languages


def extension_mapper(language: Languages) -> str:
    # mapping language to it's corresponding extension
    if language is Languages.CPP:
        return "cpp"
    if language is Languages.PYTHON:
        return "py"
    return "txt"
