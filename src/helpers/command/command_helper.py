from ...helpers.config.local_config import LocalConfig


class CommandHelper:
    @staticmethod
    def cpp_compile_command():
        return LocalConfig.read("executor.commands.cpp.compile")

    @staticmethod
    def cpp_run_command():
        return LocalConfig.read("executor.commands.cpp.run")

    @staticmethod
    def python_run_command():
        return LocalConfig.read("executor.commands.python.run")
