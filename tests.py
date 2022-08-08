#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Main Test file.
"""

import unittest

from main import DataStats, DataCapture, validate_value


class TestDataStats(unittest.TestCase):

    def setUp(self):
        values = [0,1,1,1,1,2,1,2,1]
        self.data_stats = DataStats(values)

    def test_less(self):
        self.assertEqual(self.data_stats.less(5), len([1,2,3,4]))
        self.assertEqual(self.data_stats.less(6), len([1,2,3,4,5,5]))
        self.assertEqual(self.data_stats.less(1), 0)
        self.assertEqual(self.data_stats.less(9), len([1,2,3,4,5,5,6,7,7,8]))

    def test_less_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.data_stats.less('a')

    def test_greater(self):
        self.assertEqual(self.data_stats.greater(5), len([6,7,7,8]))
        self.assertEqual(self.data_stats.greater(0), len([1,2,3,4,5,5,6,7,7,8]))
        self.assertEqual(self.data_stats.greater(8), 0)
        self.assertEqual(self.data_stats.greater(4), len([5,5,6,7,7,8]))

    def test_greater_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.data_stats.greater('a')

    def test_between(self):
        self.assertEqual(self.data_stats.between(4, 6), len([4,5,5,6]))
        self.assertEqual(self.data_stats.between(1, 1), len([1]))

        with self.assertRaises(ValueError):
            self.data_stats.between(6, 4)

        with self.assertRaises(ValueError):
            self.data_stats.between(0, 9)

    def test_between_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.data_stats.greater('a', 5)

        with self.assertRaises(TypeError):
            self.data_stats.greater(1, 'b')


class TestDataCapture(unittest.TestCase):

    def setUp(self):
        self.data_capture = DataCapture()
        self.correct_storage = [0] * 1000

    def test_add(self):
        self.data_capture.add(5)
        self.data_capture.add(1)
        self.data_capture.add(9)
        self.data_capture.add(2)
        self.data_capture.add(5)
        self.correct_storage[5] = 2
        self.correct_storage[1] = 1
        self.correct_storage[9] = 1
        self.correct_storage[2] = 1

        self.assertEqual(self.data_capture.storage, self.correct_storage)

    def test_add_not_raises_value_error(self):
        self.assertEqual(self.data_capture.add('a'), False)

    def test_add_not_raises_value_error_grater_than_1000(self):
        self.assertEqual(self.data_capture.add(1000), False)

    def test_build_stats(self):
        self.data_capture.add(5)
        self.data_capture.add(1)
        self.data_capture.add(9)
        self.data_capture.add(2)
        self.correct_storage[1] = 1
        self.correct_storage[2:4] = [2] * 3
        self.correct_storage[5:8] = [3] * 4
        self.correct_storage[9:] = [4] * 991

        stats = self.data_capture.build_stats()
        self.assertEqual(type(stats), DataStats)
        self.assertEqual(stats.storage, self.correct_storage)
        self.assertAlmostEqual(len(stats.storage), 1000)


class TestValidations(unittest.TestCase):

    def test_validate_value(self):
        self.assertEqual(True, validate_value(0, 0, 999))
        self.assertEqual(True, validate_value(999, 0, 999))
        self.assertEqual(True, validate_value(500, 0, 999))
        with self.assertRaises(ValueError):
            validate_value(1000, 0, 999)
        with self.assertRaises(ValueError):
            validate_value(-1, 0, 999)

