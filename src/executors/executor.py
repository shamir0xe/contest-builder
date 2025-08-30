from abc import ABC, abstractmethod
from collections.abc import Callable
from dataclasses import dataclass
from ..models.language import Language
from ..helpers.utils.timer import Timer
from ..models.problem import Problem
from pylib_0xe.buffer_io.buffer_writer import BufferWriter


@dataclass
class Executor(ABC):
    problem: Problem
    writer: BufferWriter
    timer: Timer = Timer()
    status: int = 0

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def language(self) -> Language:
        pass

    def attach_log(self, log: str) -> None:
        self.writer.write_line(f"\t{log}")

    def pipeline(self, *args: Callable) -> None:
        for callable in args:
            if self.status == 0:
                self.timer = Timer()
                callable()
                self.attach_log(f"time elapsed = {self.timer.timestamp()}")

    def handle_output(self, output: str) -> None:
        if len(output) > 0:
            self.attach_log("<stdout")
            self.writer.write_line(output.strip())
            self.attach_log("stdout/>")
        else:
            self.attach_log("<stdout/>")

    def handle_error(self, error: str) -> None:
        self.status = 1
        self.attach_log("<stderr")
        self.writer.write_line(error)
        self.attach_log("stderr/>")
