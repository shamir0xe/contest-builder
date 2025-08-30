from ..helpers.terminal.single_process import SingleProcess
from ..helpers.config.local_config import LocalConfig
from ..models.language import Language
from ..executors.executor import Executor
from pylib_0xe.file.file import File


class GeneralExecutor(Executor):
    def language(self) -> Language:
        return self.problem.language

    def execute(self):
        # compile the problem
        # run the problem give input to it
        self.pipeline(self.check_if_compile_is_available, self.compile, self.run)

    def check_if_compile_is_available(self):
        self.__compile_vailable = False
        compile_cmd = LocalConfig.read(
            f"executor.commands.{self.problem.language.ext}.compile"
        )
        if not compile_cmd:
            return
        self.__compile_cmd = compile_cmd
        self.__compile_vailable = True

    def compile(self):
        if not self.__compile_vailable:
            return
        self.attach_log(f"compiling {self.problem.name}...")
        command = self.__compile_cmd.format(self.problem.full_name)
        out, err = SingleProcess(command).run().communicate()
        if len(err) > 0:
            # we have an error
            self.handle_error(err)
        self.handle_output(out)

    def run(self):
        self.attach_log(f"running {self.problem.name}...")
        input_file = File.read_file(self.problem.full_input_name)
        input_file += "\r\n"
        command = LocalConfig.read(f"executor.commands.{self.problem.language.ext}.run")
        out, err = SingleProcess(command).run().communicate(input_file)
        if len(err) > 0:
            # we have an error
            self.handle_error(err)
        self.handle_output(out)
