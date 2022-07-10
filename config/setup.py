from setuptools import setup, find_packages

VERSION = '0.1'
DESCRIPTION = 'Easy python library that wraps configuration files'

setup(
    name="configfile",
    version=VERSION,
    author="Joel Nkounkou",
    author_email="",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'config', 'configuration'],
    classifiers=[
        "Programming Language :: Python :: 3"
    ]
)