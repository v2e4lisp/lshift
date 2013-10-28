#!/usr/bin/env python

from setuptools import setup

def readme():
    with open("README.rst") as it:
        return it.read()

if __name__ == '__main__':
    setup(
        name = 'lshift',
        version = '0.1.1',
        description = 'left shift args to make a function a partial application',
        long_description = readme(),
        author = "Yan Wenjun",
        author_email = "mylastnameisyan@gmail.com",
        license = 'MIT',
        url = 'https://github.com/v2e4lisp/lshift',
        py_modules = ["lshift"],
        classifiers = [
            'License :: OSI Approved :: MIT License',
            'Topic :: Software Development :: Libraries',
        ]
    )
