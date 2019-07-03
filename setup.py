from setuptools import setup, find_packages

setup(
    name='pyLDB',
    version='0.1.0',
    url='https://github.com/jwg4/pyldb',
    author='Jack Grahl',
    author_email='jack.grahl@gmail.com',
    description='Retrieve and format data from the Live Departure Board',
    packages=find_packages(),    
    install_requires=['suds-py3==1.3.3.0'],
)