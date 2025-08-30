import os
from abc import ABC
from pyfakefs.fake_filesystem import FakeFilesystem


class BaseTest(ABC):
    def change_dir(self, fs: FakeFilesystem, dir: str = "/home/user/my_project"):
        self.fake_project_dir = dir
        try:
            fs.create_dir(self.fake_project_dir)
        except Exception:
            pass
        os.chdir(self.fake_project_dir)
