import os
from src.helpers.folder.folder_helper import FolderHelper
from src.actions.extension_mapper import extension_mapper
from src.helpers.config.local_config import LocalConfig
from src.types.languages import Languages
from src.types.providers import Providers
from libs.pylib.config.config import Config
from libs.pylib.file.file import File


def extract_extension(path: str) -> str:
    index = path.rfind(".")
    if index == -1:
        return ""
    return path[index + 1 :]


def write_file(*paths: str, **kwargs) -> None:
    # extracting filename
    filename = paths[-1]
    paths = paths[:-1]

    # generating directories recursively
    FolderHelper.create_path(*paths)

    # append the file to the path
    path = os.path.join(*paths, filename)

    # write the file
    file = kwargs["file"]
    try:
        File.write_file(file_path=path, data=file)
    except Exception:
        print(f"could'nt create [{path}] file")


def read_template(provider: Providers, language: Languages) -> str:
    cfg = Config.read("defaults.config.local")
    template_path = f"{cfg}.templates.{provider.value}.{extension_mapper(language)}"
    try:
        paths: list[str] = LocalConfig.read(template_path)
    except Exception as e:
        print(e)
        exit(0)
    return File.read_file(os.path.join(*paths))
