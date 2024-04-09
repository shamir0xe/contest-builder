from __future__ import annotations
import os
from dataclasses import dataclass
from ..helpers.file.file_helper import FileHelper
from ..helpers.model.problem_helper import ProblemHelper
from ..models.contest import Contest


@dataclass
class ContestGenerator:
    contest: Contest

    def read_template(self) -> ContestGenerator:
        self.template = FileHelper.read_template(
            provider=self.contest.provider, language=self.contest.language
        )
        return self

    def build_path(self) -> ContestGenerator:
        self.contest.path = os.path.join(self.contest.provider.name, self.contest.name)
        print(f"generating the following contest\n\n{self.contest}")
        return self

    def generate_solutions(self) -> ContestGenerator:
        # generating solutions
        # solution file extension
        for i in range(self.contest.problem_cnt):
            problem_name = ProblemHelper.create_problem_name(i, self.contest.name_type)
            # {problem_name}
            # {problem_number}
            # {total_problems}
            # {provider_site}
            # {contest_name}
            solution = FileHelper.template_filler(
                self.template,
                chr(ord("A") + i),
                str(i + 1),
                str(self.contest.problem_cnt),
                self.contest.provider.name,
                self.contest.name,
            )
            # creating the solution
            FileHelper.write_file(
                self.contest.path,
                problem_name,
                f"{problem_name}.{self.contest.language.ext}",
                file=solution,
            )
        return self

    def generate_inputs(self) -> ContestGenerator:
        for i in range(self.contest.problem_cnt):
            problem_name = ProblemHelper.create_problem_name(i, self.contest.name_type)
            # creating input file
            FileHelper.write_file(
                self.contest.path,
                problem_name,
                f"{problem_name}.in",
                file="",
            )
        return self
