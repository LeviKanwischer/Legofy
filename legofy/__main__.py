# -*- coding: utf-8 -*-

"""
legofy
------

This module contains the command line interface for legofy.


    USAGE:
    $ python legofy/

See README for project details.
"""
from __future__ import absolute_import

import click
from click import Choice, Path

from legofy import legofy
from legofy import palettes


LEGOS = palettes.legos().keys()
HELP = {'image': None,
        'outfile': None,
        'size': 'Number of brick the longest side should be legofied to.',
        'dither': 'Use `dither` color approximation algorithm?',
        'palette': 'Lego Palette to be used when converting colors.'}


@click.command()
@click.argument('image', required=True, type=Path(exists=True, dir_okay=False, resolve_path=True))
@click.argument('outfile', type=Path(resolve_path=True))
@click.option('--size', '-s', type=int, help=HELP['size'])
@click.option('--palette', '-p', type=Choice(LEGOS), help=HELP['palette'])
@click.option('--dither/--no-dither', default=False, help=HELP['dither'])
def cli(image, outfile, size, palette, dither):
    """Legofy an image!"""
    legofy.convert(image, outfile, size, palette, dither)


if __name__ == '__main__':
    cli()
