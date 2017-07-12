"""The setup and basic info on String Pyramid."""
from setuptools import setup, find_packages

tests_require = [
    'pytest',
    'pytest-cov',
    'tox',
]

setup(
    name='String Pyramid',
    version='0.8',
    description='Generates a String Pyramid',
    classifiers=[
        'Programming Language :: Python',
        'Topic :: String-Pyramid :: Codewars',
    ],
    author='Alex',
    author_email='ajshort2010@hotmail.com',
    url='',
    keywords='String Pyramid',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    })
