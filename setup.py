# -*- coding: utf-8 -*-

from setuptools import setup

import legofy


def _load(filename):
    """Load file contents from package base path."""
    base = os.path.dirname(os.path.abspath(__file__))
    loadfile = os.path.join(base, filename)
    with open(loadfile, 'r') as f_in:
        return f_in.read()


README = _load('README.rst')

CLASSIFIERS = ['Development Status :: 5 - Production/Stable',
               'License :: OSI Approved :: MIT License',
               'Programming Language :: Python',
               'Programming Language :: Python :: 2.6',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3.3',
               'Programming Language :: Python :: 3.4',
               'Programming Language :: Python :: 3.5',
               'Topic :: Multimedia :: Graphics']


setup(name=legofy.__title__,
      version=legofy.__version__,
      author=legofy.__author__,
      author_email=legofy.__email__,
      url=legofy.__uri__,
      description=legofy.__summary__,
      long_description=README,
      classifiers=CLASSIFIERS,
      license=legofy.__license__,
      packages=['legofy', 'legofy.images2gif'],
      install_requires=['click>=5.1', 'pillow>=3.0.0'],
      include_package_data=True,
      entry_points={'console_scripts': ['legofy = legofy.__main__:cli']},
      package_data={'bricks': ['*.png']},
      test_suite='nose.collector',
      tests_require=['nose'])
