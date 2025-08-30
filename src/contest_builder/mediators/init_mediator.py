from __future__ import annotations
from dataclasses import dataclass

from ..mediators.base_mediator import BaseMediator
from ..helpers.config.local_config import LocalConfig
from ..helpers.file.file_helper import FileHelper
from ..helpers.config.templates import Templates
from ..helpers.config.config import Config


@dataclass
class InitMediator(BaseMediator):
    mediator_name: str = "init-mediator"

    def read_configs(self) -> InitMediator:
        self.name = Config.read("main.config.local")
        self.template_config = Templates.read(
            "contest_builder", "templates", "template.json"
        )
        return self

    def create_local_config(self) -> InitMediator:
        self.append_log(
            f"Create {self.name}.json with the following template:\n{self.template_config}"
        )
        FileHelper.write_file(f"{self.name}.json", file=self.template_config)
        return self

    def create_templates(self) -> InitMediator:
        try:
            templates = LocalConfig.read("templates")
            if not templates:
                raise Exception()
        except Exception:
            self.append_log("No templates available")
            return self
        for _, obj in templates.items():
            for _, path in obj.items():
                FileHelper.write_file(
                    *path, file=Templates.read("contest_builder", *path)
                )
        return self

    def closure(self) -> InitMediator:
        self.append_log(f"Succesfully generated {self.name} and templates")
        print(self.get_logs())
        return self
