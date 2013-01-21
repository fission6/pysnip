#!/usr/bin/env python


from setuptools import setup, find_packages
import pysnip

requires = []

setup(
    name='pysnip',
    version=pysnip.__version__,
    description='Create small text summaries or "snips" from resources.',
    long_description=open('README.rst').read(),
    author='fission6',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'straight.plugin==1.4.0-post-1',
    ],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'snip = pysnip.main:main',
        ]
    },
    classifiers=(
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),
)
