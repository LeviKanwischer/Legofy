# -*- coding: utf-8 -*-

"""
legofy
------

This module contains the command line interface for legofy.


    USAGE:
    $ python legofy/

See README for project details.
"""

import click

from legofy import legofy
from legofy import palettes


@click.command()
@click.argument('image', required=True, type=click.Path(dir_okay=False,
                                                        exists=True,
                                                        resolve_path=True))
@click.argument('outfile', default=None, required=False,
                type=click.Path(resolve_path=True))
@click.option('--size', default=None, type=int,
              help='Number of bricks the longest side of the legofied image should have.')
@click.option('--dither/--no-dither', default=False,
              help='Use dither algorithm to spread the color approximation error.')
@click.option('--palette', default=None,
              type=click.Choice(palettes.legos().keys()),
              help='Palette to use based on real Lego colors.')
def cli(image, output, size, palette, dither):
    """Legofy an image!"""
    legofy.main(image, outfile, size, palette, dither)


if __name__ == '__main__':
    cli()
