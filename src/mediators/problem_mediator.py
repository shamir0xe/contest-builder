from __future__ import annotations
from src.generators.problem_generator import ProblemGenerator
from src.helpers.model.model_helper import ModelHelper
from src.models.problem import Problem
from src.helpers.terminal.arg_helper import ArgHelper
from libs.pylib.config.config import Config


class ProblemMediator:
    def read_configs(self) -> ProblemMediator:
        self.attributes = ModelHelper.get_model_attributes(Problem)
        self.problem_data = Config.read("problem.defaults")
        return self

    def read_args(self) -> ProblemMediator:
        self.problem_data = (
            ArgHelper(
                attributes=self.attributes, 
                data=self.problem_data, 
                prefix="--"
            )
            .check_help()
            .check_args(skipps=["problem"])
            .must_include("name", "provider")
            .get_data()
        )
        return self
    
    def generate(self) -> ProblemMediator:
        problem = Problem().from_dict(self.problem_data)
        print(f"generating the following problem: {problem}")
        ProblemGenerator(problem=problem) \
            .read_template() \
            .build_path(problem_set=Config.read('defaults.problemset.folder.name')) \
            .generate_solution() \
            .generate_input() 
        return self

    def closure(self) -> ProblemMediator:
        print("DONE")
        return self
