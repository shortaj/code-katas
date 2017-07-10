"""The setup and basic info on Sudoku_Checker."""
from setuptools import setup, find_packages

tests_require = [
    'pytest',
    'pytest-cov',
    'tox',
]

setup(
    name='Sudoku_Solution_Checker',
    version='0.8',
    description='Checks Sudoku Solutions',
    classifiers=[
        'Programming Language :: Python',
        'Topic :: Sudoku :: Codewars',
    ],
    author='Alex',
    author_email='ajshort2010@hotmail.com',
    url='',
    keywords='Sudoku',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    })
