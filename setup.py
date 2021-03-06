# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "riseml"
VERSION = "0.0.1"


REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "requests"]

setup(
    name=NAME,
    version=VERSION,
    description="RiseML API client",
    author_email="contact@riseml.com",
    url="https://riseml.com",
    keywords=["RiseML"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    
    """
)