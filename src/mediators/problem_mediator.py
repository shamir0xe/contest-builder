from __future__ import annotations
from ..helpers.config.local_config import LocalConfig
from ..generators.problem_generator import ProblemGenerator
from ..models.problem import Problem
from ..helpers.terminal.arg_helper import ArgHelper


class ProblemMediator:
    def read_configs(self) -> ProblemMediator:
        self.attributes = Problem.modifiables()
        self.problem_data = LocalConfig.read("problem")
        return self

    def read_args(self) -> ProblemMediator:
        self.problem_data = (
            ArgHelper(attributes=self.attributes, data=self.problem_data, prefix="--")
            .check_help()
            .check_args(skipps=["problem"])
            .must_include("name")
            .get_data()
        )
        return self

    def generate(self) -> ProblemMediator:
        problem = Problem.from_dict(self.problem_data)
        print(f"generating the following problem: {problem}")
        ProblemGenerator(problem=problem).read_template().build_path(
            problem_set=LocalConfig.read("problemset.folder.name")
        ).generate_solution().generate_input()
        return self

    def closure(self) -> ProblemMediator:
        print("DONE")
        return self
