from setuptools import setup, find_packages

setup(
    name='pyLDB',
    version='0.3.0',
    url='https://github.com/jwg4/pyldb',
    author='Jack Grahl',
    author_email='jack.grahl@gmail.com',
    description='Retrieve and format data from the Live Departure Board',
    long_description=(
        "A package which wraps some of the fiddly parts of downloading " +
        "departure board data from the National Rail enquiries Darwin  / LDBWS " +
        "service. This code uses the suds SOAP library and the Jinja2 templating " +
        "library to allow you to input a three-letter station code and get back " +
        "HTML departure board with configurable style and layout."
    ),
    packages=find_packages(),
    install_requires=['suds-py3==1.3.3.0', 'jinja2==2.10.1'],
    tests_require=['requests'],
    include_package_data=True,
    package_data={'': ['templates/*.j2', 'pyldb/extra/css/*.css']}
)
