from setuptools import setup

setup(
    # Application name:
    name="wordhash",
    # Version number (initial):
    version="0.1.0",
    # Application author details:
    author="Jesse Bulson-Lewis",
    author_email="j.bl@posteo.org",
    # Packages
    packages=["wordhash"],
    # Include additional files into the package
    include_package_data=True,
    # Details
    url="http://pypi.python.org/pypi/MyApplication_v010/",
    license="LICENSE.md",
    description="Get a unique string of words for type of data",
    # Dependent packages (distributions)
    install_requires=[
        "bitstring",
    ],
    entry_points={
        "console_scripts": [
            "wordhash=wordhash:main",
        ]
    },
)
