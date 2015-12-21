# -*- coding: utf-8 -*-

"""Make images look as if they are made out of 1x1 LEGO blocks"""

from setuptools import setup


# TODO: Convert README to .rst & load into setup.py, .md doesn't work w/ pypi
README = ('Legofy is a python program that takes a static image or gif '
          'and makes it so that it looks as if it was built out of LEGO.')

CLASSIFIERS = ['Development Status :: 4 - Beta',
               'License :: OSI Approved :: MIT License',
               'Programming Language :: Python',
               'Programming Language :: Python :: 2.6',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3.3',
               'Programming Language :: Python :: 3.4',
               'Programming Language :: Python :: 3.5',
               'Topic :: Multimedia :: Graphics']


# TODO: Move metadata into package & load into setup.py
setup(name='legofy',
      version='2.0.0dev1',
      author='Juan Potato',
      author_email='juanpotatodev@gmail.com',
      url='https://github.com/JuanPotato/Legofy',
      description=__doc__,
      long_description=README,
      classifiers=CLASSIFIERS,
      license='MIT',
      packages=['legofy'],
      install_requires=['click>=5.1', 'pillow>=3.0.0'],
      include_package_data=True,
      entry_points={'console_scripts': ['legofy = legofy.__main__:main']},
      package_data={'bricks': ['*.png']},
      test_suite='nose.collector',
      tests_require=['nose'])
