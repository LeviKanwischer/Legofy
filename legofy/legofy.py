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
from __future__ import absolute_import, print_function

import os

from PIL import Image, ImageSequence

from legofy import images2gif
from legofy import palettes


def apply_color_overlay(image, color):
    '''Small function to apply an effect over an entire image'''
    overlay_red, overlay_green, overlay_blue = color
    channels = image.split()

    r = channels[0].point(lambda color: overlay_effect(color, overlay_red))
    g = channels[1].point(lambda color: overlay_effect(color, overlay_green))
    b = channels[2].point(lambda color: overlay_effect(color, overlay_blue))

    channels[0].paste(r)
    channels[1].paste(g)
    channels[2].paste(b)

    return Image.merge(image.mode, channels)


def overlay_effect(color, overlay):
    '''Actual overlay effect function'''
    if color < 33:
        return overlay - 100
    elif color > 233:
        return overlay + 100
    else:
        return overlay - 133 + color


def make_lego_image(thumbnail_image, brick_image):
    '''Create a lego version of an image from an image'''
    base_width, base_height = thumbnail_image.size
    brick_width, brick_height = brick_image.size

    rgb_image = thumbnail_image.convert('RGB')

    lego_image = Image.new("RGB", (base_width * brick_width,
                                   base_height * brick_height), "white")

    for brick_x in range(base_width):
        for brick_y in range(base_height):
            color = rgb_image.getpixel((brick_x, brick_y))
            lego_image.paste(apply_color_overlay(brick_image, color),
                             (brick_x * brick_width, brick_y * brick_height))
    return lego_image


def get_new_filename(file_path, ext_override=None):
    '''Returns the save destination file path'''
    folder, basename = os.path.split(file_path)
    base, extention = os.path.splitext(basename)
    if ext_override:
        extention = ext_override
    new_filename = os.path.join(folder, "{0}_lego{1}".format(base, extention))
    return new_filename


def get_new_size(base_image, brick_image, size=None):
    '''Returns a new size the first image should be so that the second one fits neatly in the longest axis'''
    new_size = base_image.size
    if size:
        scale_x, scale_y = size, size
    else:
        scale_x, scale_y = brick_image.size

    if new_size[0] > scale_x or new_size[1] > scale_y:
        if new_size[0] < new_size[1]:
            scale = new_size[1] / scale_y
        else:
            scale = new_size[0] / scale_x

        new_size = (int(round(new_size[0] / scale)) or 1,
                    int(round(new_size[1] / scale)) or 1)

    return new_size


def get_lego_palette(palette):
    '''Gets the palette for the specified lego palette mode'''
    legos = palettes.legos()
    palette = legos[palette]
    return palettes.extend_palette(palette)


def apply_thumbnail_effects(image, palette, dither):
    '''Apply effects on the reduced image before Legofying'''
    palette_image = Image.new("P", (1, 1))
    palette_image.putpalette(palette)
    return image.im.convert("P",
                        Image.FLOYDSTEINBERG if dither else Image.NONE,
                        palette_image.im)


def legofy_gif(base_image, brick_image, outfile, size, palette, dither):
    '''Alternative function that legofies animated gifs, makes use of images2gif - uses numpy!'''
    im = base_image

    # Read original image duration
    original_duration = im.info['duration']

    # Split image into single frames
    frames = [frame.copy() for frame in ImageSequence.Iterator(im)]

    # Create container for converted images
    frames_converted = []

    print("Number of frames to convert: " + str(len(frames)))

    # Iterate through single frames
    for i, frame in enumerate(frames, 1):
        print("Converting frame number " + str(i))

        new_size = get_new_size(frame, brick_image, size)
        frame.thumbnail(new_size, Image.ANTIALIAS)
        if palette:
            palette = get_lego_palette(palette)
            frame = apply_thumbnail_effects(frame, palette, dither)
        new_frame = make_lego_image(frame, brick_image)
        frames_converted.append(new_frame)

    # Make use of images to gif function
    images2gif.writeGif(outfile, frames_converted, duration=original_duration/1000.0, dither=0, subRectangles=False)

def legofy_image(base_image, brick_image, outfile, size, palette, dither):
    '''Legofy an image'''
    new_size = get_new_size(base_image, brick_image, size)
    base_image.thumbnail(new_size, Image.ANTIALIAS)
    if palette:
        palette = get_lego_palette(palette)
        base_image = apply_thumbnail_effects(base_image, palette, dither)
    make_lego_image(base_image, brick_image).save(outfile)


def main(image, outfile=None, size=None, palette=None, dither=False):
    """Legofy image or gif with brick mask."""
    here = os.path.realpath(os.path.dirname(__file__))
    brick = os.path.join(here, 'assets', 'bricks', '1x1.png')

    im = Image.open(image)
    brick = Image.open(brick)

    if dither and not palette:
        palette = 'all'

    if image.lower().endswith('.gif') and im.is_animated:
        if outfile is None:
            outfile = get_new_filename(image)
        legofy_gif(im, brick, outfile, size, palette, dither)

    else:
        # TODO: Is overriding ext necessary?
        if outfile is None:
            outfile = get_new_filename(image, '.png')
        legofy_image(im, brick, outfile, size, palette, dither)

    im.close()
    brick.close()
