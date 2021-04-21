# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 22:10:11 2020

@author: SANJAY
"""

#Random number generation

import numpy as np
def sn_random_numbers(shape, antithetic =False, moment_matching=True, fixed_seed = False):
    if fixed_seed:
        np.random.seed(1000)
    if antithetic:
        ran = np.random.standard_normal((shape[0], shape[1], shape[2] / 2))
        ran = np.concatenate((ran, -ran), axis =2)
    else:
        ran = np.random.standard_normal(shape)
    if moment_matching:
        ran = ran-np.mean(ran)
        ran = ran/np.std(ran)
    if shape[0] == 1:
        return ran[0]
    else:
        return ran
