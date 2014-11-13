import numpy as np
from sklearn.linear_model import LogisticRegression as log_reg
from utilities import *


def train(data, answer):
    log_reg_fit = log_reg(penalty='l1', C=0.010, fit_intercept=True, intercept_scaling=1)
    
    log_reg_fit.fit(data, answer)
    #print log_reg_fit.score(data, answer)
    print log_reg_fit.coef_
    return log_reg_fit

    
