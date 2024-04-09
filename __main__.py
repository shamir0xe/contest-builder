from src.mediators.contest_mediator import ContestMediator
from src.mediators.execution_mediator import ExecutionMediator
from src.mediators.problem_mediator import ProblemMediator
from src.mediators.init_mediator import InitMediator
from src.helpers.terminal.cat_helper import CatHelper
from pylib_0xe.argument.argument_parser import ArgumentParser

ARG_PREFIX = "--"


def handle_init():
    """Handle initialization."""
    InitMediator().read_configs().create_local_config().create_templates().closure()


def handle_run():
    """Handle program execution."""
    ExecutionMediator().read_configs().read_args().extract_language().extract_name().execute()


def handle_problem():
    """Handle problem solving."""
    ProblemMediator().read_configs().read_args().generate().closure()


def handle_contest():
    """Handle contest management."""
    ContestMediator().read_configs().read_args().generate().closure()


def handle_help():
    """Handle help command"""
    CatHelper.meow()


def main():
    """Main function."""
    if ArgumentParser.is_option("init", option_prefix=ARG_PREFIX):
        handle_init()
    elif ArgumentParser.is_option("run", option_prefix=ARG_PREFIX):
        handle_run()
    elif ArgumentParser.is_option("problem", option_prefix=ARG_PREFIX):
        handle_problem()
    elif ArgumentParser.is_option("name", option_prefix=ARG_PREFIX):
        handle_contest()
    else:
        handle_help()


if __name__ == "__main__":
    main()
