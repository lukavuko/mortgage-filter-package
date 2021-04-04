
from setuptools import setup, find_packages

setup(
    name='Mortgage Package',
    version='0.1',
    packages=find_packages(include=['Mortgage_Package', 'Mortgage_Package.*']),
    license='MIT',
    description='A package for filtering real estate opportunities based on your financial situation',
    url='https://github.com/lukavuko/my-mortgage',
    author='Luka Vukovic',
    author_email='luka.vuko@outlook.com'
)
    

