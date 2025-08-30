from __future__ import annotations
import os
from dataclasses import dataclass
from ..helpers.file.file_helper import FileHelper
from ..models.problem import Problem


@dataclass
class ProblemGenerator:
    problem: Problem

    def read_template(self) -> ProblemGenerator:
        self.template = FileHelper.read_template(
            provider=self.problem.provider, language=self.problem.language
        )
        return self

    def build_path(self, problem_set: str) -> ProblemGenerator:
        self.problem.problem_set = problem_set
        self.problem.path = os.path.join(
            self.problem.provider.name, problem_set, self.problem.name
        )
        return self

    def generate_solution(self) -> ProblemGenerator:
        print("generating solution")
        print(self.problem)
        # {problem_name}
        # {problem_number}
        # {total_problems}
        # {site_name}
        # {contest_name}
        solution = FileHelper.template_filler(
            self.template,
            self.problem.name,
            str(1),
            str(1),
            self.problem.provider.name,
            self.problem.problem_set,
        )
        # creating the solution
        FileHelper.write_file(
            self.problem.path,
            f"main.{self.problem.language.ext}",
            file=solution,
        )
        return self

    def generate_input(self) -> ProblemGenerator:
        FileHelper.write_file(
            self.problem.path,
            "main.in",
            file="",
        )
        return self
