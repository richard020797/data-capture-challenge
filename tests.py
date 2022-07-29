#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Main Test file.
"""

import unittest

from main import DataStats, DataCapture


class TestDataStats(unittest.TestCase):

    def setUp(self):
        values = [1,2,3,4,5,5,6,7,7,8]
        self.data_stats = DataStats(values)

    def test_less(self):
        self.assertEqual(self.data_stats.less(5), [1,2,3,4])
        self.assertEqual(self.data_stats.less(6), [1,2,3,4,5,5])
        self.assertEqual(self.data_stats.less(1), [])
        self.assertEqual(self.data_stats.less(9), [1,2,3,4,5,5,6,7,7,8])

    def test_less_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.data_stats.less('a')

    def test_greater(self):
        self.assertEqual(self.data_stats.greater(5), [6,7,7,8])
        self.assertEqual(self.data_stats.greater(0), [1,2,3,4,5,5,6,7,7,8])
        self.assertEqual(self.data_stats.greater(8), [])
        self.assertEqual(self.data_stats.greater(4), [5,5,6,7,7,8])

    def test_greater_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.data_stats.greater('a')

    def test_between(self):
        self.assertEqual(self.data_stats.between(4, 6), [4,5,5,6])
        self.assertEqual(self.data_stats.between(1, 1), [1])
        self.assertEqual(self.data_stats.between(6, 4), [])
        self.assertEqual(self.data_stats.between(0, 9), [1,2,3,4,5,5,6,7,7,8])

    def test_between_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.data_stats.greater('a', 5)

        with self.assertRaises(TypeError):
            self.data_stats.greater(1, 'b')


class TestDataCapture(unittest.TestCase):

    def setUp(self):
        self.data_capture = DataCapture()

    def test_add(self):
        self.data_capture.add(5)
        self.data_capture.add(1)
        self.data_capture.add(9)
        self.data_capture.add(2)
        self.assertEqual(self.data_capture.storage, [5,1,9,2])

    def test_add_not_raises_value_error(self):
        self.assertEqual(self.data_capture.add('a'), False)

    def test_build_stats(self):
        self.data_capture.add(5)
        self.data_capture.add(1)
        self.data_capture.add(9)
        self.data_capture.add(2)
        stats = self.data_capture.build_stats()

        self.assertEqual(type(stats), DataStats)
        self.assertEqual(stats.storage, [1,2,5,9])

