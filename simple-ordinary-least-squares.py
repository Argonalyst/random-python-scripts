# -*- coding: utf-8 -*-
"""
Created on Wed Mar 02 18:02:14 2016

@author: pedrobalmeida
"""

import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

Y = [500000, 450000, 350000, 250000, 700000, 850000, 550000]
X = [70, 68, 70, 50, 80, 90, 120]

X = sm.add_constant(X)
model = sm.OLS(Y,X)
results = model.fit()
results.params

print results.params
print results.t_test([1, 0])
print results.f_test(np.identity(2))

print results.summary()
print results.bse

stardard_deviation = results.bse[0]
print stardard_deviation

plt.plot(Y, 'r', X, 'b')
plt.ylabel('price')
plt.show()
