# Contest Builder

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

Contest Builder is a Python tool designed to simplify the process of managing programming contest solutions by providing a structured workflow for organizing, compiling, and testing code.

## Features

- Quickly generate the folder and file structure for a contest's problems.
- Customize templates for generating solution files.
- Compile and run solutions with ease.
- Test solutions for correctness.

## Table of Contents

<!-- vim-markdown-toc GFM -->

* [Installation](#installation)
* [Usage](#usage)
* [Configuration](#configuration)
* [Contributing](#contributing)

<!-- vim-markdown-toc -->

## Installation

You can install Contest Builder via pip:

```bash
pip install contest-builder
```

## Usage

0. Initializing The Workspace

   In order to specify the template files and default options for the future, you need to initialize a folder inorder
   to store the files of the contest over there.

```bash
contest-builder --init
```

- this will generate:
  1. A config file named cb-config.josn, and
  1. A template folder to put your own language specific templates there.

1. Generating Contest Structure

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

2. Compiling and Running Solutions

To compile and run a solution for a specific problem, use the contest-builder command with the --run option:

```bash
contest-builder --run <problem_name>
```

This will compile and execute the solution file for the specified problem. Also if you are located in the
problem's folder, you can discard the `<problem_name>` and just pass the `--run` option to compile and execute the code.

3. Creating Structure for Single Problem

   You can also create the folder and file structure for a single problem using the contest-builder command with the `--problem` option:

```bash
contest-builder --problem <problem_name>
```

This will generate the necessary files and directories for the specified problem.

## Configuration

Contest Builder allows you to customize templates for generating solution files. You can modify these templates according to your preferences by editing the template files located in the templates directory.

Also you need to edit the `compile` and `run` sections in the config file as you want to be done.

## Contributing

Contributions are welcome! If you have any ideas for improvements or new features, feel free to open an issue or submit a pull request.

License
Contest Builder is licensed under the MIT License. See the LICENSE file for details.
