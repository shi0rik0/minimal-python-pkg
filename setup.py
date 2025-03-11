from setuptools import setup, find_packages

setup(
    name="my-pkg",  # Name shown on PyPI
    version="0.1.0",
    # The following two lines specify that the package source code is in the `src` directory.
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        # Add dependencies here, like "numpy"
    ],
)
