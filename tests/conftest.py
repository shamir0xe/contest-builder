import pytest


@pytest.fixture
def config_main() -> str:
    return """
{
  "version": "0.0.8",
  "config": {
    "local": "cb-cfg"
  }
}
"""


@pytest.fixture
def templates_json() -> str:
    return """
{
    "contest": {
        "provider": "codeforces",
        "language": "cpp",
        "name_type": "alphabetical",
        "problem_cnt": 4
    },
    "problem": {
        "provider": "local",
        "language": "cpp"
    },
    "executor": {
        "commands": {
            "cpp": {
                "compile": "g++ -std=c++17 -O2 {} -o out",
                "run": "./out"
            },
            "python": {
                "run": "python3 {}"
            }
        }
    },
    "providers": {
        "codeforces": {
            "abbreviations": [
                "codeforces",
                "cf",
                "code"
            ]
        },
        "leetcode": {
            "abbreviations": [
                "leetcode",
                "lc",
                "leet"
            ]
        },
        "local": {
            "abbreviations": [
                "local"
            ]
        }
    },
    "languages": {
        "cpp": {
            "abbreviations": [
                "cpp",
                "c++",
                "seepp"
            ],
            "extensions": [
                "cpp",
                "hpp"
            ]
        },
        "python": {
            "abbreviations": [
                "python",
                "py",
                "python3"
            ],
            "extensions": [
                "py"
            ]
        }
    },
    "problemset": {
        "folder": {
            "name": "problemset"
        }
    },
    "templates": {}
}
"""
