from src.types.providers import Providers


def provider_finder(name: str) -> Providers:
    name = name.lower()
    if name == "lc" or name.count("leetcode") >= 1:
        return Providers.LEETCODE
    if name == "cf" or name.count("codeforces") >= 1:
        return Providers.CODEFORCES
    return Providers.LOCAL
