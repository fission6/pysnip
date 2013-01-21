#!/usr/bin/env python


from setuptools import setup, find_packages


requires = []
print find_packages()
setup(
    name='pysnip',
    version='0.1',
    description='Create small text summaries or "snips" from resources.',
    long_description=open('README.rst').read(),
    author='fission6',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'straight.plugin==1.4.0-post-1',
        'pyquery==1.2.4',
    ],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'snip = pysnip.runner:main',
        ]
    },
    classifiers=(
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),
)
