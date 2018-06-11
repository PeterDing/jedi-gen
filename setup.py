import sys

try:
    from setuptools import setup
except ImportError:
    # Use distutils.core as a fallback.
    # We won't be able to build the Wheel file on Windows.
    from distutils.core import setup

version = "0.0.1"

requires = ["jedi"]

setup(
    name="jedi-gen",
    version=version,
    author="PeterDing",
    author_email="dfhasyt@gmail.com",
    license="Apache 2.0",
    description="",
    url="http://github.com/PeterDing/jedi-gen",
    install_requires=requires,
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    packages=["jedi_gen"],
    scripts=['bin/jedi-gen'],
    include_package_data=True)
