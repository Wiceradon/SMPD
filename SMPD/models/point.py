#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Different ways of representing point.
'''


class Point(object):
    '''
    Simple model for unlabeled point in n-space
    '''

    def __init__(self, coordinates):
        '''
        Initializer with one parameter which specify coordinates of point

        :param iterable coordinates: coordinates in Cartesian space
        '''
        self.coordinates = tuple(coordinates)

    def __str__(self):
        return "Point with coordinates: {}".format(self.coordinates)

    def __eq__(self, other):
        '''
        In un-labeled point we can only distinguish between points using
        coordinates
        '''
        return self.coordinates == other.coordinates

    def _ne__(self, other):
        return not (self == other)


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
                coordinates: {}".formate(self.label, self.coordinates)

    def __eq__(self, other):
        '''
        Two point with the same position but belongings to different goups
        aren't exactly the same (ex. one of them could be a noise)
        '''
        return self.coordinates == other.coordinates \
            and self.label == other.label

    def __ne__(self, other):
        return not (self == other)
