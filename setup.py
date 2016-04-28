# encoding: utf-8

import itertools as its
from setuptools import setup, find_packages, Command
import sys, os

version = '0.7.3'


class Unit2Discover(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys, subprocess
        basecmd = ['unit2', 'discover']
        errno = subprocess.call(basecmd)
        raise SystemExit(errno)


def recursive_ls(package, directory):
    return [os.path.relpath(os.path.join(root, filename), package)
            for root, _, files in os.walk(os.path.join(package, directory))
            for filename in files]
print list(its.chain([recursive_ls('locust', 'static'),
                                           recursive_ls('locust', 'templates')]))
setup(
    name='locustio',
    version=version,
    description="Website load testing framework",
    long_description="""Locust is a python utility for doing easy, distributed load testing of a web site""",
    classifiers=[
        "Topic :: Software Development :: Testing :: Traffic Generation",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
    ],
    keywords='',
    author='Jonatan Heyman, Carl Bystrom, Joakim Hamrén, Hugo Heyman',
    author_email='',
    url='http://locust.io',
    license='MIT',
    packages=['locust', 'locust.rpc'],
    package_data={'locust': list(its.chain(recursive_ls('locust', 'static'),
                                           recursive_ls('locust', 'templates')))},
    zip_safe=False,
    install_requires=open('requirements.in').read(),
    tests_require=open('requirements.testing.in').read(),
    entry_points={
        'console_scripts': [
            'locust = locust.main:main',
        ]
    },
    test_suite='unittest2.collector',
)
