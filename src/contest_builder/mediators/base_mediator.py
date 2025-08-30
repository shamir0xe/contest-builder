from abc import ABC
from dataclasses import dataclass


@dataclass
class BaseMediator(ABC):
    mediator_name: str = "base-mediator"
    log: str = ""

    def append_log(self, log: str) -> None:
        self.log += f"[{self.mediator_name}] {log} \n"

    def get_logs(self) -> str:
        return self.log
