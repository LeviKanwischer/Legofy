******
Legofy
******
|Build Status| |PyPI Downloads| |PyPI version| |License| |Coverage Status| |Code Health| |Join the chat at https://gitter.im/JuanPotato/Legofy|

Legofy is a python package and command line utility that takes a static image or gif and makes it looks as though it was constructed out of lego bricks.

|Before| |After|


Getting Started
~~~~~~~~~~~~~~~
To install the latest stable version from `PyPI <https://pypi.python.org/pypi/legofy>`_, run ``pip install legofy``.

For the bleeding edge version, run ``pip install git+https://github.com/JuanPotato/Legofy.git``.


Usage
~~~~~
::

    Usage: legofy [OPTIONS] IMAGE OUTFILE

      Legofy an image!

    Options:
      -s, --size INTEGER              Number of brick the longest side should be
                                      legofied to.
      -p, --palette [solid|mono|all|transparent|effects]
                                      Lego Palette to be used when converting
                                      colors.
      --dither / --no-dither          Use `dither` color approximation algorithm?
      --help                          Show this message and exit.


Issues
~~~~~~
Bugs are tracked as `Issues` on Github. If you find a bug, verify an issue doesn't already `exist <https://github.com/JuanPotato/Legofy/issues>`_ before opening a new one. When creating an issue make sure to provide repo steps & a clear description to ensure the issue is understood.


Forks
~~~~~
-  JavaScript: `Legofy <https://github.com/Wildhoney/Legofy>`__

.. |Before| image:: https://raw.githubusercontent.com/JuanPotato/Legofy/master/legofy/assets/flower.jpg
    :width: 630
    :height: 930
    :scale: 50%

.. |After| image:: https://raw.githubusercontent.com/JuanPotato/Legofy/master/legofy/assets/flower_lego.png
    :width: 630
    :height: 930
    :scale: 50%

.. |Build Status| image:: https://travis-ci.org/JuanPotato/Legofy.svg?branch=master
   :target: https://travis-ci.org/JuanPotato/Legofy
.. |PyPI Downloads| image:: https://img.shields.io/pypi/dm/legofy.svg
   :target: https://pypi.python.org/pypi/legofy
.. |PyPI version| image:: https://img.shields.io/pypi/v/legofy.svg
   :target: https://pypi.python.org/pypi/legofy
.. |License| image:: https://img.shields.io/pypi/l/legofy.svg
   :target: https://pypi.python.org/pypi/legofy
.. |Coverage Status| image:: https://coveralls.io/repos/JuanPotato/Legofy/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/JuanPotato/Legofy?branch=master
.. |Code Health| image:: https://landscape.io/github/JuanPotato/Legofy/master/landscape.svg?style=flat
   :target: https://landscape.io/github/JuanPotato/Legofy/master
.. |Join the chat at https://gitter.im/JuanPotato/Legofy| image:: https://badges.gitter.im/Join%20Chat.svg
   :target: https://gitter.im/JuanPotato/Legofy?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
