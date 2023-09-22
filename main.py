from src.mediators.contest_mediator import ContestMediator
from src.mediators.execution_mediator import ExecutionMediator
from src.mediators.problem_mediator import ProblemMediator
from libs.pylib.argument.argument_parser import ArgumentParser

if __name__ == "__main__":
    if ArgumentParser.is_option("run", option_prefix="--"):
        # calling program mediator
        ExecutionMediator().read_configs().read_args().extract_language().extract_name().execute()
    elif ArgumentParser.is_option("problem", option_prefix="--"):
        # calling problem mediator
        ProblemMediator().read_configs().read_args().generate().closure()
    else:
        # calling contest mediator
        ContestMediator().read_configs().read_args().generate().closure()
