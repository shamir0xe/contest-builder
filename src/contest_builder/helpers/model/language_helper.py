from ...types.languages import Languages


class LanguageHelper:
    @staticmethod
    def extension_mapper(language: Languages) -> str:
        # mapping language to it's corresponding extension
        if language is Languages.CPP:
            return "cpp"
        if language is Languages.PYTHON:
            return "py"
        return "cpp"
