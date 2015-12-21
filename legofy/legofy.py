# -*- coding: utf-8 -*-

"""
legofy.legofy
-------------

This module contains the base codebase for legofy.


    USAGE:
    >>> from legofy import legofy
    >>> legofy.main()

See README for project details.
"""
from __future__ import absolute_import, division, print_function
# TODO: Add future/builtins to package install for 3 style range
# from builtins import range

import os

from PIL import Image, ImageSequence

from . import images2gif
from . import palettes


def apply_color_overlay(image, color):
    """Apply color effect overlay to image."""
    red, green, blue = color
    channels = image.split()

    r = channels[0].point(lambda color: overlay_effect(color, red))
    g = channels[1].point(lambda color: overlay_effect(color, green))
    b = channels[2].point(lambda color: overlay_effect(color, blue))

    channels[0].paste(r)
    channels[1].paste(g)
    channels[2].paste(b)

    return Image.merge(image.mode, channels)


def overlay_effect(color, overlay):
    """Generate color overlays."""
    if color < 33:
        return overlay - 100
    elif color > 233:
        return overlay + 100
    else:
        return overlay - 133 + color


def make_lego_image(image, brick):
    """Make legofied version of original static image."""
    image_width, image_height = image.size
    brick_width, brick_height = brick.size

    width = image_width * brick_width
    height = image_height * brick_height

    rgb = image.convert('RGB')
    lego = Image.new('RGB', (width, height), 'white')
    for x in range(image_width):
        for y in range(image_height):
            color = rgb.getpixel((x, y))
            effect = apply_color_overlay(brick, color)
            lego.paste(effect, (x*brick_width, y*brick_height))
    return lego


def get_new_filename(infile, ext=None):
    """Return save destination for missing outfile."""
    folder, basename = os.path.split(infile)
    base, extention = os.path.splitext(basename)
    extention = ext if ext else extention
    outfile = os.path.join(folder, '{}_lego{}'.format(base, extention))
    return outfile


def get_new_size(image, brick, size=None):
    """Generate legofied image size."""
    # Legofied image should fit along largest original axis
    width, height = (size, size) if size else brick.size
    image_size = image.size
    
    if image_size[0] > width or image_size[1] > height:
        if image_size[0] > image_size[1]:
            scale = image_size[0] // width
        else:
            scale = image_size[1] // height

        image_size = (image_size[0] // scale or 1, image_size[1] // scale or 1)
    return image_size


def get_lego_palette(palette):
    """Get specified palette color mapping array."""
    legos = palettes.legos()
    palette = legos[palette]
    return palettes.extend_palette(palette)


def apply_thumbnail_effects(image, palette, dither):
    """Apply effect on thumbnail image, pre legofying."""
    _image = Image.new('P', (1, 1))
    _image.putpalette(palette)
    dither = Image.FLOYDSTEINBERG if dither else Image.NONE
    return image.im.convert('P', dither, _image.im)


def convert(image, outfile=None, size=None, palette=None, dither=False):
    """Legofy image or gif with brick mask."""
    here = os.path.realpath(os.path.dirname(__file__))
    brick = os.path.join(here, 'assets', 'bricks', '1x1.png')

    if dither and not palette:
        palette = 'all'

    palette = get_lego_palette(palette) if palette else None
    outfile = outfile if outfile else get_new_filename(image)

    im = Image.open(image)
    brick = Image.open(brick)

    if image.lower().endswith('.gif') and im.is_animated:
        make_gif(im, brick, outfile, size, palette, dither)
    else:
        make_image(im, brick, outfile, size, palette, dither)

    im.close()
    brick.close()


def make_gif(image, brick, outfile, size, palette, dither):
    """Convert animated image into legofied version."""
    converted = []
    for frame in [frame.copy() for frame in ImageSequence.Iterator(image)]:
        _size = get_new_size(frame, brick, size)
        frame.thumbnail(_size, Image.ANTIALIAS)

        if palette:
            frame = apply_thumbnail_effects(frame, palette, dither)

        frame = make_lego_image(frame, brick)
        converted.append(frame)

    duration = image.info['duration'] / 1000
    images2gif.writeGif(outfile, converted, duration=duration, dither=0, subRectangles=False)


def make_image(image, brick, outfile, size, palette, dither):
    """Convert static image into legofied version."""
    _size = get_new_size(image, brick, size)
    image.thumbnail(_size, Image.ANTIALIAS)

    if palette:
        image = apply_thumbnail_effects(image, palette, dither)

    make_lego_image(image, brick).save(outfile)
