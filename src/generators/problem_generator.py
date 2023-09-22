from __future__ import annotations
import os
from dataclasses import dataclass
from src.actions.extension_mapper import extension_mapper
from src.actions.template_filler import template_filler
from src.models.problem import Problem
from src.actions.file_actions import read_template, write_file


@dataclass
class ProblemGenerator:
    problem: Problem

    def read_template(self) -> ProblemGenerator:
        self.template = read_template(
            provider=self.problem.provider, language=self.problem.language
        )
        return self

    def build_path(self, problem_set: str) -> ProblemGenerator:
        self.problem.problem_set = problem_set
        self.problem.path = os.path.join(
            self.problem.provider.value, problem_set, self.problem.name
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
        solution = template_filler(
            self.template,
            self.problem.name,
            str(1),
            str(1),
            self.problem.provider.value,
            self.problem.problem_set,
        )
        # creating the solution
        write_file(
            self.problem.path,
            f"main.{extension_mapper(self.problem.language)}",
            file=solution,
        )
        return self

    def generate_input(self) -> ProblemGenerator:
        write_file(
            self.problem.path,
            "main.in",
            file="",
        )
        return self
