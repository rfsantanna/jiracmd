from setuptools import setup
import jiracmd
import os

VERSION = jiracmd.__version__


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="jiracmd",
    description="Jira Command Line Tool",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Rafael Fernandes Sant'Anna",
    url="https://github.com/rfsantanna/jiracmd",
    project_urls={
        "Issues": "https://github.com/rfsantanna/jiracmd/issues",
        "CI": "https://github.com/rfsantanna/jiracmd/actions",
        "Changelog": "https://github.com/rfsantanna/jiracmd/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["jiracmd"],
    entry_points="""
        [console_scripts]
        jiracmd=jiracmd.cli:cli
    """,
    install_requires=["click"],
    extras_require={
        "test": ["pytest"]
    },
    python_requires=">=3.6",
)
