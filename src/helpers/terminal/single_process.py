from __future__ import annotations
import subprocess
import shlex


class SingleProcess:
    def __init__(self, *args) -> None:
        self.command = " ".join(
            [arg if isinstance(arg, str) else str(arg) for arg in args]
        )

    def run(self) -> SingleProcess:
        self.proc = subprocess.Popen(
            shlex.split(self.command),
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
