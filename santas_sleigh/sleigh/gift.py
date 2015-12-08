import numpy as np
from haversine_distance import haversine_distance

class gift(object):

    def __init__(self, latitude, longitude, weight):
        self.latitude = latitude
        self.longitude = longitude
        self.weight = weight
        return

    
    def distance(self, gift2):
        return haversine_distance(self, gift2)

    
    
