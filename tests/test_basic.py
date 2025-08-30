from src.cli import app
from unittest.mock import patch
from src.helpers.config.config import Config
from .base_test import BaseTest


class TestBasic(BaseTest):
    @patch("sys.argv", ["main.py", "--version"])
    def test_version(self, capsys):
        app()

        stdout, stderr = capsys.readouterr()

        assert Config.read("main.version") in stdout
        assert stderr == ""
