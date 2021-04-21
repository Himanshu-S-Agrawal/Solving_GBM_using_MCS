# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 11:32:43 2020

@author: Himanshu
"""


#DX Library frame
import datetime as dt
import numpy as np

def get_year_deltas(date_list, day_count = 365):
    start = date_list[0]
    delta_list = [(date-start).days/day_count for date in date_list]
    return np.array(delta_list)
