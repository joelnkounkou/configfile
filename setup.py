from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'Easy python wrapper for configuration files'

setup(
    name="configfile",
    version=VERSION,
    author="@joelnkounkou",
    author_email="",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'config', 'configuration'],
    classifiers=[
        "Programming Language :: Python :: 3"
    ]
)