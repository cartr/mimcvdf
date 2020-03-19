import sys
import os
sys.path.append('..')
import unittest
from time import time

import mimcvdf

class TestVDF(unittest.TestCase):

    def test_both(self):
        h = mimcvdf.vdf_create(b"test")
        self.assertTrue(mimcvdf.vdf_verify(b"test", h))

    def test_invalid_both(self):
        h = mimcvdf.vdf_create(b"test")
        self.assertFalse(mimcvdf.vdf_verify(b"invalid", h))

    def test_above_zero_rounds(self):
        self.assertRaises(AssertionError, mimcvdf.vdf_create, b"test", 0)
        self.assertRaises(AssertionError, mimcvdf.vdf_create, b"test", -1)
        self.assertRaises(AssertionError, mimcvdf.vdf_create, b"test", 1)
        self.assertRaises(AssertionError, mimcvdf.vdf_create, b"test", -10000)


unittest.main()