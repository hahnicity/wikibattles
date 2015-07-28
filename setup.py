#!/usr/bin/env python
from setuptools import setup, find_packages

__version__ = "0.1"


setup(
    name="wikibattles",
    author="Gregory Rehm",
    version=__version__,
    description="Ranking for all battles on wikipedia using page rank",
    packages=find_packages(),
    package_data={"*": ["*.html"]},
    install_requires=[
    ],
    entry_points={
    }
)
