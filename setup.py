# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
import os
import sys

# file read helper
def read_from_file(path):
    if os.path.exists(path):
        with open(path,"rb","utf-8") as input:
            return input.read()

setup(
    name='matomat',
    version='0.0.1',
    description='matomat is an interface for purchasing drinks in K4CG Hackerspace',
    long_description=read_from_file('README.md'),
    url='https://github.com/omgwtflaserguns/matomatpy/',
    author='omgwtflaserguns',
    author_email='info@k4cg.org',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Utilities',
        'Topic :: Terminals',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='mate mongodb fridge drinks',
    packages=find_packages(),
    zip_safe=True,
    install_requires=['pyfiglet', 'pymongo', 'dependency_injector'],
    scripts=['bin/matomat']
)
