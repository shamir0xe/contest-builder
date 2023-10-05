from __future__ import annotations
from src.helpers.config.local_config import LocalConfig
from src.helpers.file.file_helper import FileHelper
from src.helpers.config.templates import Templates
from libs.pylib.config.config import Config


class InitMediator:
    def read_configs(self) -> InitMediator:
        self.name = Config.read("main.config.local")
        self.template_config = Templates.read("templates", "template.json")
        return self

    def create_local_config(self) -> InitMediator:
        FileHelper.write_file(f"{self.name}.json", file=self.template_config)
        return self

    def create_templates(self) -> InitMediator:
        templates = LocalConfig.read("templates")
        for _, obj in templates.items():
            for _, path in obj.items():
                FileHelper.write_file(*path, file=Templates.read(*path))
        return self

    def closure(self) -> InitMediator:
        print(f"Succesfully generated {self.name} and templates")
        return self
