from ...helpers.terminal.arg_helper import ArgHelper


class CatHelper:
    @staticmethod
    def meow():
        helper = (
            ArgHelper(["name", "problem", "run", "init"])
            .check_help()
            .check_help("elp")
            .check_args()
        )
        if len(helper.get_data()) == 0:
            helper.show_valid_options().done()
