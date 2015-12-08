import numpy as np

def haversine_distance(gift1, gift2, r=1.0):
    """Haversine distance on surface of a sphere"""

    return 2*r*np.arcsin(np.sqrt(np.sin((gift2.latitude - gift1.latitude)/2.0)**2.0  + np.cos(gift1.latitude)*np.cos(gift2.latitude)*np.sin((gift2.longitude - gift1.longitude)/2.0)**2.0 ))


