from ..helpers.model.finders.language_finder import LanguageFinder
from ..executors.general_executor import GeneralExecutor
from ..executors.cpp_executor import CppExecutor
from ..executors.python_executor import PythonExecutor
from ..executors.executor import Executor
from ..models.problem import Problem
from pylib_0xe.buffer_io.buffer_writer import BufferWriter


class ProgramExecutor:
    def __init__(self, problem: Problem, writer: BufferWriter) -> None:
        self.executor: Executor | None = None
        found = False
        # CPP
        try:
            if problem.language == LanguageFinder.by_name("cpp"):
                self.executor = CppExecutor(problem, writer)
                found = True
        except Exception:
            pass

        # Python
        try:
            if problem.language == LanguageFinder.by_name("python"):
                self.executor = PythonExecutor(problem, writer)
                found = True
        except Exception:
            pass

        # General
        if not found:
            # Call the general executor
            self.executor = GeneralExecutor(problem=problem, writer=writer)

    def exe(self):
        if self.executor is not None:
            self.executor.execute()
