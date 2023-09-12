from src.helpers.terminal.single_process import SingleProcess
from src.helpers.command.command_helper import CommandHelper
from src.executors.executor import Executor


class PythonExecutor(Executor):
    def execute(self):
        # run the problem and give input to it
        self.pipeline(self.run)

    def run(self):
        self.attach_log(f"running {self.problem.name}...")
        command = CommandHelper.python_run_command()
        command.format(self.problem.full_name, self.problem.full_input_name)
        out, err = SingleProcess(command).run().communicate()
        if len(err) > 0:
            # we have an error
            self.handle_error(err)
        self.handle_output(out)


