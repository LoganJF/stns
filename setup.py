# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pip install twine

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

from stns.__version__ import __version__
# Package meta-data.
NAME = 'stns'
DESCRIPTION = 'A collection of scripts used in the Nusbaum Lab for data analysis, modeling, and visualization'
URL = 'https://github.com/LoganJF/stns' # change me
EMAIL = 'loganfickling@gmail.com'
AUTHOR = 'Logan Fickling'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = __version__ # Updated in __version__.py

# What packages are required for this module to be executed?
REQUIRED = ['scipy',
            'numpy',
            'pandas',
            'scikit-learn',#'sklearn',
            'matplotlib',
            'seaborn',
            'pandastable',
            'brian2',
            'neo',
            'mat73',
]

with open('requirements.txt') as f:
    REQUIRED = f.read().splitlines()

#
# What packages are optional?
EXTRAS = {
    # 'fancy feature': ['django'],
}

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()

except: # pragma no cover
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    with open(os.path.join(here, 'NAME__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION


class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(about['__version__']))
        os.system('git push --tags')

        sys.exit()

print(REQUIRED)
# Where the magic happens:
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],
    setup_requires=REQUIRED,
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    #license='UPenn',
    cmdclass={
        'upload': UploadCommand,
    },
)