import os


class FolderHelper:
    @staticmethod
    def create_path(*paths) -> None:
        path = ''
        for cur_path in paths:
            path = os.path.join(path, cur_path)
        os.makedirs(path)
