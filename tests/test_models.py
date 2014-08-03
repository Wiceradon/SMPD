#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_models
----------------------------------

Tests for `models` module.
"""

import unittest
from SMPD.models import distributions


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

if __name__ == '__main__':
    unittest.main()
