import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='mortgage-filter-lukavuko',
    version='0.3',
    packages=["mortgage_package"],
    license='MIT',
    description='A package for filtering real estate opportunities based on your financial situation',
    long_description=README,
    url='https://github.com/lukavuko/mortgage-filter-package',
    author='Luka Vukovic',
    author_email='luka.vuko@outlook.com',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    include_package_data=True,
    install_requires=["pandas", "numpy"]
)