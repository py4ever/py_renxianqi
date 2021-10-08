#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @PypiSeedTag: MainTest
# @Project : demo_projec5

import os
import unittest

import renxianqi.main as main


"""
generated by PypiSeed(PPC) - Unittest
"""

class MainTestCase(unittest.TestCase):
    def test_main(self):
        actual = main.main()
        expect = "hello renxianqi"
        self.assertEqual(expect, actual, "Must execute all the stages")


if __name__ == '__main__':
    unittest.main()
