<div align = 'center'>
    <h1>Contributor's Guide</h1>
    This document details guidelines contributors should follow.
</div>

## Basics:

First off, thank you for showing interest in contributing to this open-source project! As mentiomed in the `About` section, this project depends on contributors to keep it alive. To keep `hive` maintainable, we have a few requirements:

- Install all requirements needed for development as specified from ```requirements.txt```.
- Please make sure your code runs without issue on `pylint`.
- When making commits, please follow this [style guide](https://github.com/dishb/commit-styles).
- Please use v3.11.3 as the minimum version of Python.
- Your tab size should be 4 spaces; not hard tabs
- The file encoding should be UTF-8

## Development

To get started with development, read the [Getting started](./README.md#getting-started) section of the `./README.md` file.

There's a TODO file which the name says it all: list our wanted features. You can pick one and start working!

A separate branch from "main" is recommended. After you finish your work, make a PR on GitHub and I will look for that.

## Linting

To lint your code with `pylint`, run the following commands from the top-level directory of the repository:
```bash
pylint $(git ls-files '*.py') --rcfile=.pylintrc
```
