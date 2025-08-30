from pylib_0xe.file.file import File
from pylib_0xe.path.path_helper import PathHelper


class Templates:
    @staticmethod
    def read(*args: str) -> str:
        return File.read_file(
            PathHelper.from_root(__file__, root_name="contest_builder", *args)
        )
