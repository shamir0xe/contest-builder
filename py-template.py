from __future__ import annotations
import os, io

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


class Mediator:
    def read_input(self) -> Mediator:
        return self

    def solve(self) -> Mediator:
        return self

    def print_output(self) -> None:
        pass


def main():
    Mediator().read_input().solve().print_output()


if __name__ == "__main__":
    main()
