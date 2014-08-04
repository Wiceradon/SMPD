#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Different ways of representing point.
'''
import numpy as np


class Point(object):
    '''
    Simple model for unlabeled point in n-space
    '''

    def __init__(self, coordinates):
        '''
        Initializer with one parameter which specify coordinates of point

        :param 1D array coordinates: coordinates in Cartesian space
        '''
        self.coordinates = np.copy(coordinates)
        if not self.coordinates.size:
            raise ValueError("Construction param must not be empty") 

    def __str__(self):
        return "Point with coordinates: {}".format(self.coordinates)

    def __eq__(self, other):
        '''
        In un-labeled point we can only distinguish between points using
        coordinates
        '''
        if other.__class__ != Point:
            raise ValueError("Compare only unlabelled points")
        return np.array_equal(self.coordinates, other.coordinates)

    def _ne__(self, other):
        return not (self == other)

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Point(self.coordinates + other)
        if other.__class__ == Point:
            return Point(self.coordinates + other.coordinates)
        raise ValueError('Only integer/float/Point addition supported')

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Point(self.coordinates * other)
        if other.__class__ == Point:
            return Point(self.coordinates * other.coordinates)
        raise ValueError('Only integer/float/Point addition supported')

    def __rmul__(self, other):
        return self.__mul__(other)


class LabeledPoint(Point):
    '''
    Extension of :class Point with main purpose of representing classified
    point.
    '''

    def __init__(self, coordinates, label):
        '''
        Initializer

        :param iterable coordinates: coordinates of a point in Cartesian space
        :param label: representaion of a group to which point belong
        '''
        super(LabeledPoint, self).__init__(coordinates)
        self.label = label

    def __str__(self):
        return "Point from group {} with \
                coordinates: {}".format(self.label, self.coordinates)

    def __eq__(self, other):
        '''
        Two point with the same position but belongings to different goups
        aren't exactly the same (ex. one of them could be a noise)
        '''
        return self.coordinates == other.coordinates \
            and self.label == other.label

    def __ne__(self, other):
        return not (self == other)
