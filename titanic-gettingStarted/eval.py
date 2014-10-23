import sys
from utilities import *

choice='logistic'

if choice=='logistic':
    from logistic import *



print train([], np.array([1,4,12,3,3]))
