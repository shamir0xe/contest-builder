from __future__ import annotations
from ..helpers.config.local_config import LocalConfig
from ..helpers.terminal.arg_helper import ArgHelper
from ..generators.contest_generator import ContestGenerator
from ..models.contest import Contest


class ContestMediator:
    def read_configs(self) -> ContestMediator:
        self.attributes = Contest.modifiables()
        self.contest_data = LocalConfig.read("contest")
        return self

    def read_args(self) -> ContestMediator:
        self.contest_data = (
            ArgHelper(attributes=self.attributes, data=self.contest_data, prefix="--")
            .check_help()
            .check_args(skipps=[])
            .must_include("name")
            .get_data()
        )
        return self

    def generate(self) -> ContestMediator:
        contest: Contest = Contest.from_dict(self.contest_data)
        ContestGenerator(
            contest=contest
        ).read_template().build_path().generate_solutions().generate_inputs()
        return self

    def closure(self) -> ContestMediator:
        print("DONE")
        return self
