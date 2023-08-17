from __future__ import annotations
from libs.pylib.config.config import Config
from libs.pylib.argument.argument_parser import ArgumentParser
from src.generators.contest_generator import ContestGenerator
from src.actions.name_type_mapper import name_type_mapper
from libs.pylib.data.data_transfer_object import DataTransferObject


class ContestMediator:
    def read_configs(self) -> ContestMediator:
        self.attributes = Config.read("defaults").keys()
        self.contest = DataTransferObject()
        self.contest.site = Config.read("defaults.site")
        self.contest.name = Config.read("defaults.name", default=None)
        self.contest.name_type = Config.read("defaults.name_type")
        self.contest.problem_cnt = Config.read("defaults.problem_cnt")
        self.contest.template_path = Config.read("defaults.template_path")
        return self

    def read_args(self) -> ContestMediator:
        for key in ArgumentParser.get_options():
            key = key.lower()
            value = ArgumentParser.get_value(key)
            if key == 'help' or not hasattr(self.contest, key):
                print(f'available options are: {list(self.attributes)}')
                exit(0)
            if not hasattr(self.contest, key) or value is None:
                continue
            setattr(self.contest, key, value[0])
        if getattr(self.contest, "name") is None:
            print("Error: Enter the contest name with --name")
            exit(0)
        return self

    def generate(self) -> ContestMediator:
        self.contest.name_type = name_type_mapper(self.contest.name_type)
        print(f'generating the following contest\n\n{self.contest}')
        ContestGenerator() \
            .set_site(self.contest.site) \
            .set_folder(self.contest.name) \
            .read_template(self.contest.template_path) \
            .generate_solutions(
                count=int(self.contest.problem_cnt), 
                name_type=self.contest.name_type
            ) \
            .generate_inputs()
        return self
    
    def closure(self) -> ContestMediator:
        print(f'DONE')
        return self
