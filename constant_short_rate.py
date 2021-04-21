# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 11:43:13 2020

@author: Himanshu
"""

from get_year_deltas import *
import numpy as np

class constant_short_rate(object):
    # class for constant short rate discounting.
    #attributes: name, short rate
    #mthods: get_discount_factors
    
    def __init__(self, name, short_rate):
        self.name = name
        self.short_rate = short_rate
        if short_rate<0:
            raise ValueError('Short rate negative')
            
    def get_discount_factors(self, date_list, dtobjects=True):
        if dtobjects is True:
            dlist = get_year_deltas(date_list)
        else:
            dlist = np.array(date_list)
        dflist = np.exp(self.short_rate*np.sort(-dlist))
        return np.array((date_list, dflist)).T
    
        