from setuptools import setup, find_packages

setup(
    name='status_package',
    version='0.1.0',
    description='A simple Flask status checker',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'psutil',
        'pymongo'
    ],
    entry_points={
        'console_scripts': []
    }
)
