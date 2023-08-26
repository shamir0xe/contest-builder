import os
from libs.pylib.file.file import File


def extract_extension(path: str) -> str:
    index = path.rfind(".")
    if index == -1:
        return ""
    return path[index + 1 :]


def write_file(*paths: str, **kwargs) -> None:
    # generating directories recursively
    path = ""
    for cur_path in paths[:-1]:
        path = os.path.join(path, str(cur_path))
    try:
        os.makedirs(path)
    except Exception:
        pass

    # append the file to the path
    path = os.path.join(path, str(paths[-1]))

    # write the file
    file = kwargs["file"]
    try:
        File.write_file(file_path=path, data=file)
    except Exception:
        print(f"coudlnt create [{path}] file")
