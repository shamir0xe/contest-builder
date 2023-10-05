# from src.mediators.contest_mediator import ContestMediator
# from src.mediators.execution_mediator import ExecutionMediator
# from src.mediators.problem_mediator import ProblemMediator
from src.mediators.init_mediator import InitMediator
from libs.pylib.argument.argument_parser import ArgumentParser

ARG_PREFIX = "--"


if __name__ == "__main__":
    if ArgumentParser.is_option("init", option_prefix=ARG_PREFIX):
        InitMediator().read_configs().create_local_config().create_templates().closure()
    elif ArgumentParser.is_option("run", option_prefix=ARG_PREFIX):
        # calling program mediator
        # ExecutionMediator().read_configs().read_args().extract_language().extract_name().execute()
        pass
    elif ArgumentParser.is_option("problem", option_prefix=ARG_PREFIX):
        # calling problem mediator
        # ProblemMediator().read_configs().read_args().generate().closure()
        pass
    else:
        # calling contest mediator
        # ContestMediator().read_configs().read_args().generate().closure()
        pass
