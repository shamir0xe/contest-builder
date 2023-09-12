from __future__ import annotations
from libs.pylib.buffer_io.standard_output_buffer import StandardOutputBuffer
from src.executors.program_excecutor import ProgramExecutor
from libs.pylib.buffer_io.buffer_writer import BufferWriter
from src.models.problem import Problem
from libs.pylib.argument.argument_parser import ArgumentParser
from src.actions.problem_actions import set_problem_name, set_problem_language


class ExecutionMediator:
    def __init__(self) -> None:
        pass

    def read_configs(self) -> ExecutionMediator:
        return self

    def read_args(self) -> ExecutionMediator:
        value = ArgumentParser.get_value("run", option_prefix="--")
        if value is not None:
            # retrieving the problem based on the given name
            self.problem = Problem().from_dict({"path": value})
        else:
            # finding problem base on directory
            self.problem = Problem()
        return self

    def extract_language(self) -> ExecutionMediator:
        set_problem_language(self.problem)
        return self

    def extract_name(self) -> ExecutionMediator:
        set_problem_name(self.problem)
        return self

    def execute(self) -> ExecutionMediator:
        ProgramExecutor(self.problem, BufferWriter(StandardOutputBuffer())).exe()
        return self
