from src.cli import handle_version, handle_init
import os
from unittest.mock import patch
from src.helpers.config.config import Config


class TestBasic:
    @patch("sys.argv", ["main.py", "--version"])
    def test_version(self, capsys):
        handle_version()

        stdout, stderr = capsys.readouterr()

        assert Config.read("main.version") in stdout
        assert stderr == ""

    @patch("sys.argv", ["main.py", "--init"])
    def test_init(self, fs, capsys, config_main, templates_json):
        fs.create_file(
            f"{os.path.dirname(__file__)}/../configs/main.json", contents=config_main
        )
        fs.create_file(
            f"{os.path.dirname(__file__)}/../templates/template.json",
            contents=templates_json,
        )

        fake_project_dir = "/home/user/my_project"
        fs.create_dir(fake_project_dir)

        os.chdir(fake_project_dir)
        assert os.getcwd() == fake_project_dir

        handle_init()

        stdout, stderr = capsys.readouterr()
        assert stderr == ""
        assert "Succesfully generated" in stdout

        filename = Config.read("main.config.local")
        assert os.path.exists(f"{filename}.json")
