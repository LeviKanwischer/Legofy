# -*- coding: utf-8 -*-

"""
legofy.images2gif
-----------------

Contains images2gif versions for both py2 & py3.


    USAGE:
    $ legofy.images2gif.*

See p2/py3 for acknowledgements & copyrights.
"""

import sys

# TODO: Merge into single source, currently split due to binary data
if sys.version_info.major == 3:
    from .py3 import *
else:
    from .py2 import *
