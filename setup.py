#!/usr/bin/env python3

import setuptools  # type: ignore

META = dict(
    name="grader",
    version="0.1.0",
    description="TODO: write a description",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/fmind/grader",
    author="Médéric Hurier (fmind)",
    author_email="fmind@fmind.me",
    license="LGPL-3.0",
    packages=["grader"],
    keywords="sample package development",
    classifiers=["Development Status :: 4 - Beta"],
    entry_points={"console_scripts": ["grader=grader.__main__:main"]},
    python_requires=">=3.7",
    install_requires=[
        'mimesis',
        'voila',
        'dash',
    ],
)

if __name__ == "__main__":
    setuptools.setup(**META)
