from ..helpers.model.finders.language_finder import LanguageFinder
from ..models.language import Language
from ..models.problem import Problem
from pylib_0xe.file.file import File


class ProblemActions:
    @staticmethod
    def set_problem_language(problem: Problem) -> Language:
        all_files = File.get_all_files(directory=problem.path)
        for filename in all_files:
            extension = filename[filename.rfind(".") + 1 :]
            for language in LanguageFinder.all():
                if extension in language.extensions:
                    problem.language = language
                    problem.language.ext = extension
                    return language
        raise Exception("Solution not found!")

    @staticmethod
    def set_problem_name(problem: Problem) -> str:
        filename = File.get_all_files(directory=problem.path, ext=problem.language.ext)[
            0
        ]
        problem.name = filename[: filename.rfind(".")]
        return problem.name
