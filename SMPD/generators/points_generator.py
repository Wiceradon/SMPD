# -*- coding: utf-8 -*-


class Generator(object):
    '''
    Class used for generating list of N points in M dimennsions (M features).
    '''

    ERRORS = {-1: "Feature size must be positive", -2: "Number of class must \
be positive"}

    def __init__(self, possible_coordinates):
        '''
        Simplest initializer it sets only number_of_classes.

        :param possible_coordinates: 2D list of possible coordinate that point
        can have. It cannot be None or empty.
        '''
        if not possible_coordinates:
            raise ValueError("Construction param must not be empty")
        for i in possible_coordinates:
            if not i:
                raise ValueError("Construction param cannot has empty\
 sub-array")
        self.number_of_classes = len(possible_coordinates)
        self.default_class_size = None
        self.number_of_features = None
        self.possible_coordinates = possible_coordinates
