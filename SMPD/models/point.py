# -*- coding: utf-8 -*-

class point(object):
    '''
    Simple model for unlabeled point in n-space
    '''

    def __init__(self, features):
        '''
        Initializer with one parameter which specify coordinates of point

        :param tuple features: coordinates in Cartesian space
        '''
        self.coordinates = tuple(features)

    def __str__(self):
        return "Point with coordinates: {}".format(self.coordinates)

    def __eq__(self, other):
        return self.coordinates == other.coordinates

    def _ne__(self, other):
        return not (self == other)
