# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 11:12:58 2021

@author: hreed
"""

# Plots of some data

import numpy as np
import matplotlib.pyplot as plt

def fun(x, mu, sig):
    return 1/(sig*np.sqrt(2*np.pi))*np.exp(-1/2*((x-mu)/sig)**2)

x = np.linspace(0,100, 100)

y_s = np.zeros(len(x))
y = np.zeros(len(x))
for i in range(len(x)):
    y_s[i] = fun(x[i], 65.1, 10.5)
    y[i] = fun(x[i], 65.8, 9.7)
    
    
plt.plot(x,y_s, 'r', label = "Severe")
plt.plot(x, y, 'b', label = "Mild")
plt.title("Age Distributions")
plt.xlabel("Age")
plt.ylabel("Probability")
plt.legend()
plt.show()