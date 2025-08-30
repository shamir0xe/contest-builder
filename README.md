<h1 align="center" style="display: block; font-size: 2.5em; font-weight: bold; margin-block-start: 1em; margin-block-end: 1em; border: none;">
<a name="logo" href="#"><img align="center" src="https://github.com/shamir0xe/contest-builder/blob/main/assets/contest-builder.jpg?raw=true" alt="contest-builder" style="width:66%;"/></a>
<br/><br/><strong>Contest Builder</strong>
</h1>


![Python](https://img.shields.io/badge/Python-3.12.3%2B-blue)
[![CI Pipeline](https://github.com/shamir0xe/contest-builder/actions/workflows/ci.yaml/badge.svg?branch=main)](https://github.com/shamir0xe/contest-builder/actions/workflows/ci.yaml)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

Contest Builder is a CLI tool designed to simplify the process of managing programming contest solutions by providing a structured workflow for organizing, compiling, and testing code.

## Features

- Quickly generate the folder and file structure for a contest's problems.
- Customize templates for generating solution files.
- Compile and run solutions with ease.
- Test solutions for correctness.

## Table of Contents

<!-- vim-markdown-toc GFM -->

* [Installation](#installation)
* [Usage](#usage)
  * [Initializing The Workspace](#initializing-the-workspace)
  * [Generating Contest Structure](#generating-contest-structure)
  * [Compiling and Running Solutions](#compiling-and-running-solutions)
  * [Creating Structure for Single Problem](#creating-structure-for-single-problem)
* [Configuration](#configuration)
* [Contributing](#contributing)
* [License](#license)

<!-- vim-markdown-toc -->

## Installation

You can install Contest Builder via pip:

```bash
pip install contest-builder
```

## Usage

### Initializing The Workspace

In order to specify the template files and default options for the future, you need to initialize a folder inorder
to store the files of the contest over there.

```bash
contest-builder --init
```

- this will generate:
  1. A config file named `cb-config.json`, and
  1. A `templates` folder which stores language specific templates.

### Generating Contest Structure

To generate the folder and file structure for a contest, use the contest-builder command with the `--name` option:

```bash
contest-builder --name <contest_name>
```

This will create the necessary directories and files for each problem in the contest, using the provided templates.
You can specify the details of the contest by passing other options as well. The list of all options are as follow:

- `--provider <site_provider>`
  You need to specify the website that provides the contest in the config file first. There are some default values
  as well like `codeforces` and `leetcode`.
- `--problem_cnt <problem_count>`
  Specify the number of problems.
- `--language <programming_language>`
  Specify the language you are using at this contest if it differs from the default value.
- `--name_type <folders_name_type>`
  It can be `alphabetical`, `numerical`, or `roman`.

For example you want to create a codeforces contest with 8 problems, using python language. in order to do this, you
can simply write:

```bash
contest-builder --name "Codeforces Round 938 (Div. 3)" --problem_cnt 8 --language py --provider cf
```

You can set your desired abbreviations for languages and contest providers in the `cb-config`.

### Compiling and Running Solutions

To compile and run a solution for a specific problem, use the contest-builder command with the --run option:

```bash
contest-builder --run <problem_name>
```

This will detect the language you've chosen to write the code, and then
compiles and executes the solution based on the way it's provided in the
`cb-config`. If you are located in the
problem's folder, you can discard the `<problem_name>` and just pass the `--run` option.

Example:

```bash
contest-builder --run a
```

### Creating Structure for Single Problem

   You can also create the folder and file structure for a single problem using the contest-builder command with the `--problem` option:

```bash
contest-builder --problem --name <problem_name>
```

This will generate the necessary files and directories for the specified problem.

Example:

```bash
contest-builder --problem --name "Random Problem" --language seepp --provider lc
```

it will generate `leetcode/problemset/random-problem/random-problem.cpp` and it's
corresponding input as well.

## Configuration

Contest Builder allows you to customize templates for generating solution files. You can modify these templates according to your 
preferences by editing the template files located in the `templates` directory or adding the new ones for other languages.

Also you need to edit the `compile` and `run` sections in the config file as you wish.

## Contributing

Contributions are welcome! If you have any ideas for improvements or new features, feel free to open an issue or submit a pull request.

## License

Contest Builder is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
