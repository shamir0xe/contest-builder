from ..executors.cpp_executor import CppExecutor
from ..executors.python_executor import PythonExecutor
from ..executors.executor import Executor
from ..models.problem import Problem
from pylib_0xe.buffer_io.buffer_writer import BufferWriter


class ProgramExecutor:
    def __init__(self, problem: Problem, writer: BufferWriter) -> None:
        self.executor: Executor | None = None
        if problem.language == CppExecutor.language():
            self.executor = CppExecutor(problem, writer)
        if problem.language == PythonExecutor.language():
            self.executor = PythonExecutor(problem, writer)

    def exe(self):
        if self.executor is not None:
            self.executor.execute()
