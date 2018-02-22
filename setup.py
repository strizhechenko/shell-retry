# coding: utf-8
import os
from setuptools import setup


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths)) as f:
        return f.read()


setup(
    name='shell-retry',
    version='0.0.6',
    packages=['shell_retry'],
    url='https://github.com/strizhechenko/shell-retry',
    license='MIT',
    author='Oleg Strizhechenko',
    author_email='oleg.strizhechenko@gmail.com',
    description='Wrapper for call any utilities with retries until they succeed',
    long_description=(read('README.rst')),
    entry_points={
        'console_scripts': [
            'shell-retry=shell_retry.__init__:main',
        ],
    },
)
