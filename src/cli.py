from .helpers.config.config import Config
from .mediators.contest_mediator import ContestMediator
from .mediators.execution_mediator import ExecutionMediator
from .mediators.problem_mediator import ProblemMediator
from .mediators.init_mediator import InitMediator
from .helpers.terminal.cat_helper import CatHelper
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


def handle_version():
    """Print out the CLI version"""
    print(f"current cli version is: {Config.read("main.version")}")


def handle_help():
    """Handle help command"""
    CatHelper.meow()


def app():
    """Main app function."""
    if ArgumentParser.is_option("init", option_prefix=ARG_PREFIX):
        handle_init()
    elif ArgumentParser.is_option("run", option_prefix=ARG_PREFIX):
        handle_run()
    elif ArgumentParser.is_option("problem", option_prefix=ARG_PREFIX):
        handle_problem()
    elif ArgumentParser.is_option("name", option_prefix=ARG_PREFIX):
        handle_contest()
    elif ArgumentParser.is_option("version", option_prefix=ARG_PREFIX):
        handle_version()
    else:
        handle_help()
