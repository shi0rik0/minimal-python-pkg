# A minimal example of a Python package

## File structure

I will explain the purpose of the core files.

### `pyproject.toml`

This file specifies that we are using `setuptools` as the build system.

### `setup.py`

This script is executed by `setuptools` to install or build the package. It specifies metadata like the package name, version, and dependencies.

### `src/my_pkg`

This directory contains the source code of the package. It is a convention to put the source code under a directory named `src`.

## Development

To install the package in development mode, run:

```bash
pip install -e .
```

This command installs the package in "editable" mode, which means that changes to the source code are immediately reflected in the installed package.

You can run the following command to test the installation:

```bash
python -c "import my_pkg; my_pkg.hello_world()"
```

## Building

To build the package, first you need to install a package named `build`:

```bash
pip install build
```

Then, run:

```bash
python -m build
```

The built artifacts will be stored in the `dist/` directory.

## Uploading to PyPI

To upload the package to PyPI, you need to install a package named `twine`:

```bash
pip install twine
```

Then, run:

```bash
twine upload dist/*
```

You will be asked to enter your API token. You can create one on your PyPI account page.
