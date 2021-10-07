#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path

from setuptools import setup

setup(
    name="balaboba",
    version="1.0.2",
    description="Module for interacting with Yandex Balaboba",
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/monosans/balaboba",
    author="monosans",
    author_email="hsyqixco@protonmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    packages=["balaboba"],
    python_requires=">=3.6",
    include_package_data=True,
    install_requires=["requests"],
)
