import platform

from ...types.platforms import Platforms


class PlatformHelper:
    @staticmethod
    def get_platform() -> Platforms:
        for cur_platform in Platforms:
            if cur_platform.name.lower() == platform.system().lower():
                return cur_platform
        return Platforms.LINUX
