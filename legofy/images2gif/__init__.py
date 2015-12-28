# -*- coding: utf-8 -*-

"""
legofy.images2gif
-----------------

Contains images2gif versions for both py2 & py3.


    USAGE:
    >>> from legofy import images2gif
    >>> images2gif.writeGif(*args)

See p2/py3 for acknowledgements & copyrights.
"""
from __future__ import absolute_import

import sys

# TODO: Merge into single source, currently split due to binary data
if sys.version_info[0] < 3:
    from images2gif.py2 import writeGif
else:
    from images2gif.py3 import writeGif
