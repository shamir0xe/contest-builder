from libs.pylib.config.config import Config


class CommandHelper:
    @staticmethod
    def cpp_compile_command():
        return Config.read("executor.commands.cpp.compile")

    @staticmethod
    def cpp_run_command():
        return Config.read("executor.commands.cpp.run")

    @staticmethod
    def python_run_command():
        return Config.read("executor.commands.python.run")
