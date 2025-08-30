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
def general_program_content() -> str:
    return """
package main

import "fmt"

func main() {
	fmt.Println("Hello World!")
}
"""


@pytest.fixture
def templates_json() -> str:
    return """
{
  "author": "shamir0xe",
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
        "compile": "g++ -std=c++17 -O2 -w {} -o out",
        "run": "./out"
      },
      "python": {
        "run": "python3 {}"
      },
      "go": {
        "compile": "go build -o out {}",
        "run": "./out"
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
    "atcoder": {
      "abbreviations": [
        "atcoder",
        "at",
        "atc"
      ]
    },
    "codewars": {
      "abbreviations": [
        "codewars",
        "cw",
        "codew"
      ]
    },
    "usaco": {
      "abbreviations": [
        "usaco",
        "usa"
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
    },
    "go": {
      "abbreviations": [
        "go"
      ],
      "extensions": [
        "go"
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
