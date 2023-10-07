from __future__ import annotations
from src.actions.problem_actions import ProblemActions
from src.executors.program_excecutor import ProgramExecutor
from src.models.problem import Problem
from libs.pylib.buffer_io.standard_output_buffer import StandardOutputBuffer
from libs.pylib.buffer_io.buffer_writer import BufferWriter
from libs.pylib.argument.argument_parser import ArgumentParser


class ExecutionMediator:
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
        ProblemActions.set_problem_language(self.problem)
        return self

    def extract_name(self) -> ExecutionMediator:
        ProblemActions.set_problem_name(self.problem)
        return self

    def execute(self) -> ExecutionMediator:
        print(f'going to execute {self.problem}')
        ProgramExecutor(self.problem, BufferWriter(StandardOutputBuffer())).exe()
        return self
