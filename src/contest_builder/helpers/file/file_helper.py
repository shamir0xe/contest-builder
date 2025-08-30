import os
from ...models.language import Language
from ...models.provider import Provider
from ...helpers.folder.folder_helper import FolderHelper
from ...helpers.config.local_config import LocalConfig
from pylib_0xe.file.file import File
from pylib_0xe.buffer_io.buffer_reader import BufferReader
from pylib_0xe.buffer_io.string_buffer import StringBuffer


class FileHelper:
    @staticmethod
    def extract_extension(path: str) -> str:
        index = path.rfind(".")
        if index == -1:
            return ""
        return path[index + 1 :]

    @staticmethod
    def write_file(*paths: str, **kwargs: str) -> None:
        # extracting filename
        filename = paths[-1]
        paths = paths[:-1] if len(paths) > 1 else ()

        # generating directories recursively
        FolderHelper.create_path(*paths)

        # append the file to the path
        path = os.path.join(*paths, filename)

        # write the file
        file = kwargs["file"]
        try:
            File.write_file(file_path=path, data=file)
        except Exception as e:
            print(f"could'nt create [{path}] file")
            print(e)

    @staticmethod
    def read_template(provider: Provider, language: Language) -> str:
        paths: list[str] = LocalConfig.read(
            f"templates.{provider.name}.{language.name}"
        )
        return File.read_file(os.path.join(*paths))

    @staticmethod
    def template_filler(template: str, *args: str) -> str:
        reader = BufferReader(StringBuffer(template))
        taken = 0
        page = ""
        while not reader.end_of_buffer():
            line = reader.next_line()
            if taken < len(args):
                cnt = line.count("{}")
                if cnt > 0:
                    try:
                        line = line.format(*args[taken : taken + cnt])
                        taken += cnt
                    except Exception as e:
                        print(e)
            page += line
        return page
