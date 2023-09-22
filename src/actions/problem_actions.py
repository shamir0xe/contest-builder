from libs.pylib.config.config import Config
from libs.pylib.file.file import File
from src.models.problem import Problem
from src.types.languages import Languages
from src.types.name_types import NameTypes
from src.actions.extension_mapper import extension_mapper


def create_problem_name(idx: int, name_type: NameTypes) -> str:
    if name_type is NameTypes.ALPHABETICAL:
        return chr(ord("a") + idx)
    elif name_type is NameTypes.NUMERICAL:
        return f"{idx + 1}"
    elif name_type is NameTypes.ROMAN:
        # TODO
        return ""
    return ""


def set_problem_language(problem: Problem) -> Languages:
    all_files = File.get_all_files(directory=problem.path)
    for filename in all_files:
        extension = filename[filename.rfind(".") + 1 :]
        for language in Languages:
            if extension in Config.read(f"executor.extension_mapper.{language.value}"):
                problem.language = language
                return language
    raise Exception("Solution not found!")


def set_problem_name(problem: Problem) -> str:
    filename = File.get_all_files(
        directory=problem.path, ext=extension_mapper(problem.language)
    )[0]
    problem.name = filename[: filename.rfind(".")]
    return problem.name
