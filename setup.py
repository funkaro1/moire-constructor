from setuptools import setup, find_packages

setup(
    name='Moirepattern',
    version='alpha-0.0.2',
    packages=find_packages(),
    description='A lib to generate Moire patterns',
    author='IE Barrera',
    author_email='iebarrer@uc.cl',
    url = "https://github.com/funkaro1/moire-constructor",
    install_requires = ['shapely', 'PyQt5']
)