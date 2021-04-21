# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 22:25:26 2021

@author: Himanshu
"""
import datetime as dt
from dx_frame import *

me_gbm = market_environment('me_gbm', dt.datetime(2020,1,1))

me_gbm.add_constant('initial_value', 36)
me_gbm.add_constant('volatility', 0.1)
me_gbm.add_constant('final_date', dt.datetime(2020,12,31))
me_gbm.add_constant('currency', 'EUR')
me_gbm.add_constant('frequency', 'M')
me_gbm.add_constant('paths', 10000)
csr = constant_short_rate('csr', 0.05)
me_gbm.add_curve('discount_curve', csr)
gbm = geometric_brownian_motion('gbm', me_gbm)
gbm.generate_time_grid()
paths_1 = gbm.get_instrument_values()

gbm.update(volatility=0.5)
paths_2 = gbm.get_instrument_values(fixed_seed = False)

import matplotlib.pyplot as plt
plt.figure(figsize=(8,4))
p1 = plt.plot(gbm.time_grid, paths_1[:,:15], 'b')
p2 = plt.plot(gbm.time_grid, paths_2[:,:15], 'r-.')
plt.grid(True)
l1 = plt.legend([p1[0], p2[0]], ['low_volatility', 'high_volatility'], loc =2)
plt.gca().add_artist(l1)
plt.xticks(rotation=30)
plt.show()