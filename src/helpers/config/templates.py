from libs.pylib.file.file import File
from libs.pylib.path.path_helper import PathHelper


class Templates:
    @staticmethod
    def read(*args: str) -> str:
        return File.read_file(PathHelper.from_root(*args))
