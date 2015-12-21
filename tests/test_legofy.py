# -*- coding: utf-8 -*-

"""
Unit tests for legofy


    USAGE:
    $ nosetests tests
    ... or
    $ nosetests tests.test_legofy:Create.test_legofy_image

See README for project details.
"""

import os
import tempfile
import unittest

from PIL import Image

from legofy import legofy
from legofy import palettes


HERE = os.path.realpath(os.path.dirname(__file__))
ASSETS = os.path.join(HERE, '..', 'legofy', 'assets')
FLOWER = os.path.join(ASSETS, 'flower.jpg')
BACON = os.path.join(ASSETS, 'bacon.gif')


class Create(unittest.TestCase):
    """Unit tests that create files."""

    def setUp(self):
        self.outfile = None

    def tearDown(self):
        if self.outfile:
            os.remove(self.outfile)

    def create_tmpfile(self, suffix):
        """Creates a temporary file and stores the path in self.outfile"""
        handle, self.outfile = tempfile.mkstemp(prefix='lego_', suffix=suffix)
        os.close(handle)
        self.assertTrue(os.path.exists(self.outfile))
        self.assertTrue(os.path.getsize(self.outfile) == 0)

    # TODO: Move repeated asset check into seperate function

    def test_legofy_image(self):
        """Can we legofy a static image?"""
        self.create_tmpfile('.png')
        self.assertTrue(os.path.exists(FLOWER), 'Could not find image : %s' % FLOWER)
        legofy.main(FLOWER, outfile=self.outfile)
        self.assertTrue(os.path.getsize(self.outfile) > 0)

    def test_legofy_gif(self):
        """Can we legofy an animated image?"""
        self.create_tmpfile('.gif')
        self.assertTrue(os.path.exists(BACON), 'Could not find image : %s' % BACON)
        legofy.main(BACON, outfile=self.outfile)
        self.assertTrue(os.path.getsize(self.outfile) > 0)

    def test_legofy_palette(self):
        """Can we use palettes?"""
        self.create_tmpfile('.png')
        self.assertTrue(os.path.exists(FLOWER), 'Could not find image : %s' % FLOWER)
        for palette in palettes.legos():
            legofy.main(FLOWER, outfile=self.outfile, palette_mode=palette)
        self.assertTrue(os.path.getsize(self.outfile) > 0)

    def test_bricks_parameter(self):
        """Can we specify --brick parameter?"""
        self.create_tmpfile('.png')
        legofy.main(FLOWER, outfile=self.outfile, size=5)
        size5 = os.path.getsize(self.outfile)
        legofy.main(FLOWER, outfile=self.outfile, size=10)
        size10 = os.path.getsize(self.outfile)
        self.assertTrue(size5 > 0)
        self.assertTrue(size5 < size10)

    def test_small_brick(self):
        """Test hitting the minimal brick size"""
        self.create_tmpfile('.png')
        legofy.main(FLOWER, outfile=self.outfile, size=1)
        self.assertTrue(Image.open(self.outfile).size == (30, 30))

    def test_dither_without_palette(self):
        """Dithering without a palette should still work"""
        self.create_tmpfile('.png')
        legofy.main(FLOWER, outfile=self.outfile, dither=True)
        self.assertTrue(os.path.getsize(self.outfile) > 0)


class Functions(unittest.TestCase):
    """Test the behaviour of individual functions"""

    def test_get_new_filename(self):
        """Test the default output filename generation"""
        # Is the generated path in the same directory?
        new_path = legofy.get_new_filename(FLOWER)
        self.assertTrue(os.path.dirname(FLOWER) == os.path.dirname(new_path))
        # Is the generated path unique?
        self.assertFalse(os.path.exists(new_path), 'Should not find image: %s' % new_path)
        # Test default file extensions
        self.assertTrue(new_path.endswith('_lego.jpg'))
        new_path = legofy.get_new_filename(FLOWER, '.gif')
        self.assertTrue(new_path.endswith('_lego.gif'))

    def test_lego_palette_structure(self):
        """Validate lego palettes structured in 3's."""
        legos = palettes.legos()
        for palette in legos:
            self.assertFalse(len(legos[palette]) % 3)

    def test_lego_palette_length(self):
        """PIL palette requires 768 ints (256 colors * RGB)."""
        for palette in palettes.legos():
            self.assertTrue(len(palettes.extend_palette(palette)) == 768)


class Failures(unittest.TestCase):
    """Make sure things fail when they should"""

    def test_bad_image_path(self):
        """Test invalid image path"""
        fake_path = os.path.join(HERE, 'fake_image.jpg')
        self.assertFalse(os.path.exists(fake_path), 'Should not find image: %s' % fake_path)
        self.assertRaises(SystemExit, legofy.main, fake_path)


if __name__ == '__main__':
    unittest.main()
