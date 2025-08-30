from ..helpers.model.finders.language_finder import LanguageFinder
from ..models.language import Language
from ..helpers.terminal.single_process import SingleProcess
from ..helpers.command.command_helper import CommandHelper
from ..executors.executor import Executor
from pylib_0xe.file.file import File


class CppExecutor(Executor):
    def language(self) -> Language:
        return LanguageFinder.by_abbreviation("cpp")

    def execute(self):
        # compile the problem
        # run the problem give input to it
        self.pipeline(self.compile, self.run)

    def compile(self):
        self.attach_log(f"compiling {self.problem.name}...")
        command = CommandHelper.cpp_compile_command()
        command = command.format(self.problem.full_name)
        out, err = SingleProcess(command).run().communicate()
        if len(err) > 0:
            # we have an error
            self.handle_error(err)
        self.handle_output(out)

    def run(self):
        self.attach_log(f"running {self.problem.name}...")
        # command = CommandHelper.cpp_run_command()
        # command = command.format(self.problem.full_input_name)
        input_file = File.read_file(self.problem.full_input_name)
        input_file += "\r\n"
        out, err = (
            SingleProcess(CommandHelper.cpp_run_command()).run().communicate(input_file)
        )
        if len(err) > 0:
            # we have an error
            self.handle_error(err)
        self.handle_output(out)
