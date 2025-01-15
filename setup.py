#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="Faker",
    version="1.0.0",
    description="Faker is a Python package that generates fake data for you.",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/faker",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.8",
    install_requires=[
        "python-dateutil>=2.4",
        "typing_extensions",
    ],
    zip_safe=False,
)
