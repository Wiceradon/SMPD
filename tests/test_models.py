#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_models
----------------------------------

Tests for `models` module.
"""

import unittest
import numpy as np
from SMPD.models import distributions
from SMPD.models import points

class test_gaussian(unittest.TestCase):

    def setUp(self):
        self.deviation_generator =\
            distributions.GaussianDistribution.init_from_deviation(3, 2)
        self.variance_generator = distributions.GaussianDistribution(3, 5)

    def test_deviation_init(self):
        assert self.deviation_generator.variance == 4, 'Incorrect conversion \
is {} - should be {}'. format(self.deviation_generator.variance, 4)

    def test_generation_size(self):
        generator = self.variance_generator.generate_value(3)
        assert len(next(generator)) == 3, 'Incorrect size'
        assert len(next(generator)) == 3, 'Incorrect size'
        generator = self.variance_generator.generate_value(0)
        assert len(next(generator)) == 0, 'Incorrect size'


class test_point(unittest.TestCase):

    def test_eq(self):
        simple_3d_point = points.Point([1, 2, 3])
        numpy_3d_point = points.Point(np.array([1, 2, 3]))
        other_3d_point = points.Point([2, 2, 2])
        simple_4d_point = points.Point([1, 2, 3, 4])

        # Check if simple array and numpy are eq
        assert simple_3d_point == numpy_3d_point, 'simple array and numpy\
should be equal!'
        # Check same # dimensions but different values
        assert simple_3d_point != other_3d_point, 'Error, coordinates are\
different but objects are equal!'
        # Check different dimensions
        assert simple_3d_point != simple_4d_point, 'Error, dimensions are\
different but objects are equal!'

    def test_copy(self):
        coord = np.array([1, 2, 3])
        point1 = points.Point([1, 2, 3])
        point2 = points.Point(coord)
        coord[0] = 2

        assert point1 == point2, 'Error, copy didn\'t worked!'

    def test_addition(self):
        p1 = points.Point([1, 2, 3])
        p2 = points.Point([2, 3, 4])
        scalar = 2
        vect_add = points.Point([3, 5, 7])
        scalar_add = points.Point([3, 4, 5])
        
        res1 = p1 + p2
        assert res1 == vect_add, 'Error, result of addtion is\
{}'.format(res1.coordinates)
        res1 = p1 + scalar
        assert res1 == scalar_add, 'Error, result of addition is\
{}'.format(res1.coordinates)
        
        try:
            res1 = p1 + "as"
            assert True == False, 'Error, string added to point'
        except ValueError:
            pass

    def test_multiplication(self):
        p1 = points.Point([1, 2, 3])
        p2 = points.Point([2, 3, 4])
        scalar = 2
        vect_mul = points.Point([2, 6, 12])
        scalar_mul = points.Point([2, 4, 6])
        
        res1 = p1 * p2
        assert res1 == vect_mul, 'Error, result of multiplication is\
{}'.format(res1.coordinates)
        res1 = p1 * scalar
        assert res1 == scalar_mul, 'Error, result of multiplication is\
{}'.format(res1.coordinates)
        
        try:
            res1 = p1 * "as"
            assert True == False, 'Error, string multiplied with point'
        except ValueError:
            pass


if __name__ == '__main__':
    unittest.main()
