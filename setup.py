from setuptools import setup, find_packages

setup(
    name="pythreagile",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'pyyaml',
        'pytest',
    ],
)