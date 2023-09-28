from __future__ import annotations
from src.helpers.terminal.arg_helper import ArgHelper
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
        self.contest_data = (
            ArgHelper(
                attributes=self.attributes, 
                data=self.contest_data, 
                prefix="--"
            )
            .check_help()
            .check_args(skipps=[])
            .must_include("name")
            .get_data()
        )
        return self

    def generate(self) -> ContestMediator:
        contest: Contest = Contest().from_dict(self.contest_data)
        print(f"generating the following contest\n\n{contest}")
        ContestGenerator(contest=contest) \
            .read_template() \
            .build_path() \
            .generate_solutions() \
            .generate_inputs()
        return self

    def closure(self) -> ContestMediator:
        print("DONE")
        return self
