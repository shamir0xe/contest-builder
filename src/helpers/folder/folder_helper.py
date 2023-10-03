import os


class FolderHelper:
    @staticmethod
    def create_path(*args: str) -> None:
        path = os.path.join(*args)
        try:
            # print(f"path: {path}")
            os.makedirs(path, exist_ok=True)
        except Exception as e:
            print(f"Error: {e}")
