# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 14:20:47 2021

@author: hreed
"""

# Read in data as matrices

# Check data

s = []
s.append(1)
print(s)

def check_age(data, lower_bound, upper_bound, col):
    '''
    Verify that the data in column col is in the given range (lower_bound, upper_bound)

    Parameters
    ----------
    data : an np.array matrix where the rows are cases and the columns are features
    lower_bound : lower bound of feature in column col
    upper_bound : upper bound of feature in column col
    col : the column we are checking

    Returns
    -------
    The rows that do not pass our check

    '''
    
    


