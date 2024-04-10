from __future__ import annotations
import subprocess
import shlex

from ...helpers.type.platform_helper import PlatformHelper
from ...types.platforms import Platforms


class SingleProcess:
    def __init__(self, *args) -> None:
        self.command = " ".join(
            [arg if isinstance(arg, str) else str(arg) for arg in args]
        )
        if Platforms.WINDOWS is PlatformHelper.get_platform():
            # if the platform is windows, just split
            self.command_list = self.command.split(" ")
        else:
            # otherwise, use shlex to separate comments, etc...
            self.command_list = shlex.split(self.command)

    def run(self) -> SingleProcess:
        self.proc = subprocess.Popen(
            self.command_list,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            bufsize=1,
            universal_newlines=True,
        )
        return self

    def communicate(self, input: str = "") -> tuple[str, str]:
        stdout, stderr = self.proc.communicate(input=input)
        return self.stringify(stdout), self.stringify(stderr)

    @staticmethod
    def stringify(buffer) -> str:
        if buffer is None:
            return ""
        res = ""
        for line in buffer:
            res += line
        return res
