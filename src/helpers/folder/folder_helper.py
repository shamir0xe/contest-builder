import os


class FolderHelper:
    @staticmethod
    def create_path(*args: str) -> None:
        if len(args) == 0:
            return
        path = os.path.join(*args)
        try:
            os.makedirs(path, exist_ok=True)
        except Exception as e:
            print(f"Error: {e}")
