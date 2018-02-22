from setuptools import setup

setup(
    name='shell-retry',
    version='0.0.1',
    packages=['shell_retry'],
    url='https://github.com/strizhechenko/shell-retry',
    license='MIT',
    author='Oleg Strizhechenko',
    author_email='oleg.strizhechenko@gmail.com',
    description='Wrapper for call any utilities with retries until they succeed',
    entry_points={
        'console_scripts': [
            'shell-retry=shell_retry.__init__:main',
        ],
    },
)
