import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Don't import analytics-python module here, since deps may not be installed
# sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pymarketo'))

# OLD DO NOT USE:
# python setup.py register -r pypi
# python setup.py sdist upload -r pypi

# NEW PYPI UPLOAD METHOD:
# python setup.py sdist
# twine upload dist/*

long_description = '''
Marketo Python REST is a Python client that wraps the Marketo Rest API.
Originally developed by asamat with contributions from sandipsinha and osamakhn
'''

setup(
    name='marketorestpython',
    version= '1.5.8',
    url='https://github.com/Ajaymamgain/marketo-rest-python',
    author='Ajay Mamgain',
    author_email='jep@castelein.net',
    packages=['marketorestpython', 'marketorestpython.helper'],
    license='MIT License',
    install_requires=[
        'backoff',
        'requests',
        'pytz'
    ],
    keywords = ['Marketo', 'REST API', 'Wrapper', 'Client'],
    description='Python Client for the Marketo REST API',
    long_description=long_description
)
