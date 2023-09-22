from __future__ import annotations
from src.helpers.model.model_helper import ModelHelper
from src.generators.contest_generator import ContestGenerator
from src.models.contest import Contest
from libs.pylib.config.config import Config
from libs.pylib.argument.argument_parser import ArgumentParser


class ContestMediator:
    def read_configs(self) -> ContestMediator:
        self.attributes = ModelHelper.get_model_attributes(Contest)
        self.contest_data = Config.read("defaults")
        return self

    def read_args(self) -> ContestMediator:
        for key, value in ArgumentParser.get_options(option_prefix="--").items():
            key = key.lower()
            # help option resolver
            if key == "help" or not hasattr(Contest, key):
                print(f"available options are: {self.attributes}")
                exit(0)
            if value == "":
                continue
            self.contest_data[key] = value
        if "name" not in self.contest_data or self.contest_data["name"] == "":
            print("Error: Enter the contest name with --name")
            exit(0)
        return self

    def generate(self) -> ContestMediator:
        contest: Contest = Contest().from_dict(self.contest_data)
        print(f"generating the following contest\n\n{contest}")
        ContestGenerator().set_site(contest.site).set_folder(
            contest.name
        ).read_template(contest.template_path).generate_solutions(
            count=int(contest.problem_cnt), name_type=contest.name_type
        ).generate_inputs()
        return self

    def closure(self) -> ContestMediator:
        print("DONE")
        return self
