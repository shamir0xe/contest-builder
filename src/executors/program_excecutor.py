from src.executors.cpp_executor import CppExecutor
from src.executors.python_executor import PythonExecutor
from src.executors.executor import Executor
from libs.pylib.buffer_io.buffer_writer import BufferWriter
from src.models.problem import Problem
from src.types.languages import Languages


class ProgramExecutor:
    def __init__(self, problem: Problem, writer: BufferWriter) -> None:
        self.executor: Executor|None = None
        if problem.language is Languages.CPP:
            self.executor = CppExecutor(problem, writer)
        if problem.language is Languages.PYTHON:
            self.executor = PythonExecutor(problem, writer)

    def exe(self):
        if self.executor is not None:
            self.executor.execute()
