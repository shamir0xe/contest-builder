from __future__ import annotations
import os
from dataclasses import dataclass
from src.actions.extension_mapper import extension_mapper
from src.actions.file_actions import read_template, write_file
from src.models.contest import Contest
from src.actions.problem_actions import create_problem_name
from src.actions.template_filler import template_filler


@dataclass
class ContestGenerator:
    contest: Contest

    def read_template(self) -> ContestGenerator:
        self.template = read_template(
            provider=self.contest.provider, language=self.contest.language
        )
        return self

    def build_path(self) -> ContestGenerator:
        self.contest.path = os.path.join(self.contest.provider.value, self.contest.name)
        print(f"generating the following contest\n\n{self.contest}")
        return self

    def generate_solutions(self) -> ContestGenerator:
        # generating solutions
        # solution file extension
        extension = extension_mapper(self.contest.language)
        for i in range(self.contest.problem_cnt):
            problem_name = create_problem_name(i, self.contest.name_type)
            # {problem_name}
            # {problem_number}
            # {total_problems}
            # {provider_site}
            # {contest_name}
            solution = template_filler(
                self.template,
                chr(ord("A") + i),
                str(i + 1),
                str(self.contest.problem_cnt),
                self.contest.provider.value,
                self.contest.name,
            )
            # creating the solution
            write_file(
                self.contest.path,
                problem_name,
                f"{problem_name}.{extension}",
                file=solution,
            )
        return self

    def generate_inputs(self) -> ContestGenerator:
        for i in range(self.contest.problem_cnt):
            problem_name = create_problem_name(i, self.contest.name_type)
            # creating input file
            write_file(
                self.contest.path,
                problem_name,
                f"{problem_name}.in",
                file="",
            )
        return self
