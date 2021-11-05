# Mccabe

[![image](https://img.shields.io/github/license/long2ice/mccabe)](https://github.com/long2ice/mccabe)
[![image](https://github.com/long2ice/mccabe/workflows/ci/badge.svg)](https://github.com/long2ice/mccabe/actions?query=workflow:ci)
[![image](https://coveralls.io/repos/github/mccabe/mccabe/badge.svg)](https://coveralls.io/github/long2ice/mccabe)

## Introduction

Calculate the cyclomatic complexity of the source code.

Current supported languages:

- [Go](https://github.com/tree-sitter/tree-sitter-go)
- [Python](https://github.com/tree-sitter/tree-sitter-javascript)
- [JavaScript](https://github.com/tree-sitter/tree-sitter-python)

## Installation

Because don't publish to pypi, you can install from source code.

```shell
pip install git+https://github.com/long2ice/mccabe.git
```

## Usage

You can use `mccabe` in both `cli` and `program`.

### Use in cli

```shell
> mcc --help
Usage: mcc [OPTIONS]

  Calculate the cyclomatic complexity of the source code

Options:
  -V, --version              Show the version and exit.
  -d, --directory TEXT       The source code directory
  -f, --file TEXT            The source code file
  -l, --language [py|go|js]  The source code language  [required]
  --help                     Show this message and exit.
```

### For single file

You can calculate the cyclomatic complexity for single source file.

```shell
> mcc -l py -f tests/test_languages.py
{
    "tests/test_languages.py": 9
}
```

### For directory

You can also calculate the cyclomatic complexity for directory, which will do parallel computing.

```shell
> mcc -l py -d tests
{
    "tests/test_languages.py": 9,
    "tests/__init__.py": 0,
    "tests/test_provider.py": 4,
    "tests/test_cyclomaticc_complexity.py": 8,
    "tests/sources/py.py": 24
}
```

### Use in program

Also, you can use it in program.

```python
from mcc import get_provider_class
from mcc.languages import Lang

cls = get_provider_class(Lang.py)
ret = cls(file="test.py")
print(ret)
```

## Benchmark

## Develop

### Clone

First you clone the repo.

```shell
git clone https://github.com/long2ice/mccabe.git
```

### Install deps

Then install the requirements.

```shell
make deps
```

### Check CI

Before you commit, you should check the code style and syntax.

```shell
make style ci
```

## License

This project is licensed under the [Apache-2.0](./LICENSE) License.
