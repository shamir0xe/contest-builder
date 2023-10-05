import os
from src.helpers.model.language_helper import LanguageHelper
from src.helpers.folder.folder_helper import FolderHelper
from src.helpers.config.local_config import LocalConfig
from src.types.languages import Languages
from src.types.providers import Providers
from libs.pylib.config.config import Config
from libs.pylib.file.file import File
from libs.pylib.buffer_io.buffer_reader import BufferReader
from libs.pylib.buffer_io.string_buffer import StringBuffer


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
    def read_template(provider: Providers, language: Languages) -> str:
        cfg = Config.read("defaults.config.local")
        template_path = f"{cfg}.templates.{provider.value}.\
        {LanguageHelper.extension_mapper(language)}"
        try:
            paths: list[str] = LocalConfig.read(template_path)
        except Exception as e:
            print(e)
            exit(0)
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
