#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

setup_requirements = [
    # 'pytest-runner',
    # TODO(cyrilpic): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    # 'pytest',
    # TODO: put package test requirements here
]

setup(
    name='space_filling_designs',
    version='0.1.0',
    description="Space fillings designs for modern DOE",
    long_description=readme,
    author="Cyril Picard",
    author_email='cyril.picard@epfl.ch',
    url='https://github.com/cyrilpic/space_filling_designs',
    packages=find_packages(include=['space_filling_designs']),
    # entry_points={
    #     'console_scripts': [
    #         'space_filling_designs=space_filling_designs.cli:main'
    #     ]
    # },
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='space_filling_designs',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
