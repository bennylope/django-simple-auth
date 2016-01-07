# -*- coding: utf-8 -*-

import os
import sys
import simple_auth

from setuptools import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()


with open('README.rst') as f:
    readme = f.read()


setup(
    name='django-simple-auth',
    version=simple_auth.__version__,
    description='Simple password-only protection',
    long_description=readme,
    author='Ben Lopatin',
    author_email='ben@benlopatin.com',
    url='https://github.com/bennylope/django-simple-auth',
    license='BSD License',
    packages=[
        'simple_auth',
        'simple_auth.migrations',
    ],
    platforms=['OS Independent'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
    ],
    include_package_data=True,
)
