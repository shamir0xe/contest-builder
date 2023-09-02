from __future__ import annotations
from src.types.name_types import NameTypes
from libs.pylib.file.file import File
from src.actions.file_actions import extract_extension, write_file
from src.actions.problem_actions import create_problem_name
from src.actions.template_filler import template_filler


class ContestGenerator:
    def set_site(self, site_name: str) -> ContestGenerator:
        self.site_name = site_name
        return self

    def set_folder(self, contest_name: str) -> ContestGenerator:
        self.contest_name = contest_name
        return self

    def read_template(self, path: str) -> ContestGenerator:
        self.template = File.read_file(path)
        self.ext = extract_extension(path)
        return self

    def generate_solutions(self, count: int, name_type: NameTypes) -> ContestGenerator:
        self.count = count
        self.name_type = name_type
        for i in range(count):
            problem_name = create_problem_name(i, name_type)
            # {problem_name}
            # {problem_number}
            # {total_problems}
            # {site_name}
            # {contest_name}
            template = template_filler(
                self.template,
                chr(ord("A") + i),
                str(i + 1),
                str(count),
                self.site_name,
                self.contest_name,
            )
            # creating template
            write_file(
                self.site_name,
                self.contest_name,
                problem_name,
                f"{problem_name}.{self.ext}",
                file=template,
            )
        return self

    def generate_inputs(self) -> ContestGenerator:
        for i in range(self.count):
            problem_name = create_problem_name(i, self.name_type)
            # creating input file
            write_file(
                self.site_name,
                self.contest_name,
                problem_name,
                f"{problem_name}.in",
                file="",
            )

        return self
