#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    'matplotlib'
]

test_requirements = [
]

setup(
    name='sudokusolver',
    version='0.1.0',
    description='Sudoku Solver is a Python program to solve Sudoku puzzle. It implements the recursive backtracking algorithm. It also plots the journey to the solution and a couple of statistics.',
    long_description=readme + '\n\n' + history,
    author='Krishnakumar Ramamoorthy',
    author_email='ipower2@yahoo.com',
    url='https://github.com/ipower2/sudokusolver',
    packages=[
        'sudokusolver',
    ],
    package_dir={'sudokusolver':
                 'sudokusolver'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='sudokusolver',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
