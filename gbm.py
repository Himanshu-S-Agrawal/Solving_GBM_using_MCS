# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 18:31:28 2021

@author: Himanshu
"""

#Geometric brownian motion

import numpy as np

from sn_random_numbers_gen import sn_random_numbers
from generic_simulation_class import simulation_class

class geometric_brownian_motion(simulation_class):
    #class to generate simiulated paths usinig gbm
    # attriibutes: name, mar_env, corr
    #methods: update(to update parameters), generate_paths
    def __init__(self, name, mar_env, corr=False):
        super().__init__(name, mar_env, corr)
    
    def update(self, initial_value = None, volatility=None, final_date=None):
        if initial_value is not None:
            self.initial_value = initial_value
        if volatility is not None:
            self.volatility = volatility
        if final_date is not None:
            self.final_date = final_date
    
    
    def generate_paths(self, fixed_seed = False, day_count = 365):
        if self.time_grid is None:
            self.generate_time_grid()
            
        M = len(self.time_grid)
        J = self.paths
        paths = np.zeros((M,J))
        paths[0] = self.initial_value
        if not self.correlated:
            rand = sn_random_numbers((1,M,J), fixed_seed=fixed_seed)
        else:
            rand = self.random_numbers
            
        short_rate = self.discount_curve.short_rate
        for t in range(1, len(self.time_grid)):
            if not self.correlated:
                ran = rand[t]
            else:
                ran = np.dot(self.cholesky_matrix, rand[:, t, :])
                ran = ran[self.rn_set]
            dt = (self.time_grid[t]-self.time_grid[t-1]).days/day_count
            paths[t] = paths[t-1]*np.exp((short_rate-0.5*self.volatility**2)*dt + self.volatility*np.sqrt(dt)*ran)
        self.instrument_values = paths    
    
    