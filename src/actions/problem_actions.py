from src.helpers.model.finders.language_finder import LanguageFinder
from src.models.language import Language
from src.models.problem import Problem
from libs.pylib.file.file import File


class ProblemActions:
    @staticmethod
    def set_problem_language(problem: Problem) -> Language:
        all_files = File.get_all_files(directory=problem.path)
        for filename in all_files:
            extension = filename[filename.rfind(".") + 1 :]
            for language in LanguageFinder.all():
                if extension in language.extensions:
                    problem.language = language
                    return language
        raise Exception("Solution not found!")

    @staticmethod
    def set_problem_name(problem: Problem) -> str:
        filename = File.get_all_files(
            directory=problem.path,
            ext=problem.language.ext
        )[0]
        problem.name = filename[: filename.rfind(".")]
        return problem.name 
