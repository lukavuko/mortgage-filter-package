
from setuptools import setup, find_packages

setup(
    name='Mortgage Package',
    version='0.3',
    packages=find_packages(include=['mortgage_package', 'mortgage_package.*']),
    license='MIT',
    description='A package for filtering real estate opportunities based on your financial situation',
    url='https://github.com/lukavuko/mortgage-filter-package',
    author='Luka Vukovic',
    author_email='luka.vuko@outlook.com'
)
    

