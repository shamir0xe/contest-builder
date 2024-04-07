from functools import partial
from src.mediators.contest_mediator import ContestMediator
from src.mediators.execution_mediator import ExecutionMediator
from src.mediators.problem_mediator import ProblemMediator
from src.mediators.init_mediator import InitMediator
from pylib_0xe.argument.argument_parser import ArgumentParser

ARG_PREFIX = "--"

# Mapping command-line options to handler functions
option_handlers = {
    "init": partial(
        InitMediator().read_configs().create_local_config().create_templates().closure
    ),
    "run": partial(
        ExecutionMediator()
        .read_configs()
        .read_args()
        .extract_language()
        .extract_name()
        .execute
    ),
    "problem": partial(ProblemMediator().read_configs().read_args().generate().closure),
    "contest": partial(ContestMediator().read_configs().read_args().generate().closure),
}


def main():
    """Main function."""
    option = ArgumentParser.get_option(option_prefix=ARG_PREFIX)
    if option in option_handlers:
        option_handlers[option]()
    else:
        print("Invalid option")


if __name__ == "__main__":
    main()
