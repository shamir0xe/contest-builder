import os
from unittest.mock import MagicMock, patch
from pyfakefs.fake_filesystem import FakeFilesystem
from pytest_mock import MockerFixture
from tests.base_test import BaseTest
from src.contest_builder.helpers.config.local_config import LocalConfig
from src.contest_builder.helpers.config.config import Config
from src.contest_builder.helpers.file.file_helper import FileHelper
from src.contest_builder.cli import app, handle_init


class TestExecutor(BaseTest):
    def project_init(self, fs: FakeFilesystem, config_main, templates_json):
        fs.create_file(
            f"{os.path.dirname(__file__)}/../src/contest_builder/configs/main.json",
            contents=config_main,
        )
        fs.create_file(
            f"{os.path.dirname(__file__)}/../src/contest_builder/templates/template.json",
            contents=templates_json,
        )
        handle_init()

    @patch("sys.argv", ["main.py", "--init"])
    def test_init(self, fs: FakeFilesystem, capsys, config_main, templates_json):
        self.change_dir(fs)
        assert os.getcwd() == self.fake_project_dir

        self.project_init(fs=fs, config_main=config_main, templates_json=templates_json)

        stdout, stderr = capsys.readouterr()
        assert stderr == ""
        assert "generated" in stdout

        filename = Config.read("main.config.local")
        assert os.path.exists(f"{filename}.json")

    @patch("sys.argv", ["main.py", "--run"])
    def test_run_general_program(
        self,
        mocker: MockerFixture,
        fs: FakeFilesystem,
        general_program_content,
        capsys,
        config_main,
        templates_json,
    ):
        sp_compile = MagicMock()
        sp_compile.run.return_value = sp_compile
        sp_compile.communicate.return_value = "", ""

        sp_run = MagicMock()
        sp_run.run.return_value = sp_run
        sp_run.communicate.return_value = "Hello World!", ""

        mock_class = mocker.patch(
            "src.contest_builder.executors.general_executor.SingleProcess"
        )
        mock_class.side_effect = [sp_compile, sp_run]

        self.change_dir(fs)
        self.project_init(fs, config_main, templates_json)
        capsys.readouterr()

        self.change_dir(fs, "/home/user/my_project/random_problems")
        FileHelper.write_file("main.go", file=general_program_content)
        FileHelper.write_file("main.in", file="")
        app()

        expected_calls = [
            mocker.call(LocalConfig.read(f"executor.commands.go.run")),
            mocker.call(
                LocalConfig.read(f"executor.commands.go.compile").format("./main.go")
            ),
        ]
        mock_class.assert_has_calls(expected_calls, any_order=True)  # type: ignore
        sp_run.run.assert_called_once()
        sp_compile.run.assert_called_once()

        _, stderr = capsys.readouterr()
        assert stderr == ""
