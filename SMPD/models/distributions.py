#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Different way of algorithmically getting random variable
'''
import numpy as np


class GaussianDistribution(object):
    '''
    The Gaussian (normal) distribution is very commonly used for getting
    variable around some expected value and with some variance.
    '''

    def __init__(self, mean, variance):
        '''
        Initializer which takes three standard parameters for computing normal
        distribution

        :param float mean: Expected value of distribution
        :param float variance: How generated values should vary from expected
        value (how much they are spread out)
        '''
        self.mu = mean
        self.variance = variance

    @classmethod
    def init_from_deviation(cls, mean, st_deviation):
        '''
        Inititalizer which takes two parameters and computes third one.

        :param float mean: Expected value of distribution
        :param float st_deviation: Standard deviation - Amount of
        dipertion from average
        '''
        return cls(mean, st_deviation ** 2)

    def generate_value(self, size):
        '''
        Function returning generator for creating normal distributed values

        :param integer size: How many random numbers should be generated
        '''
        while True:
            yield np.random.normal(self.mu, self.variance, size)
