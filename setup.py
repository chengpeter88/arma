from setuptools import setup, find_packages

setup(
    name='arma',
    version='1.0.0',
    description=' ARMA, AR amd MA model process',
    author='Peter_Cheng',
    packages=find_packages(),
    install_requires=['numpy', 'pandas', 'matplotlib',"openpyxl"],
)