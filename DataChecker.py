# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 14:20:47 2021

@author: hreed
"""

import numpy as np

def check_range(data, lower_bound, upper_bound, col, remove = True):
    '''
    Verify that the data in column col is in the given range (lower_bound, upper_bound)

    Parameters
    ----------
    data : an np.array matrix where the rows are cases and the columns are features
    lower_bound : lower bound of feature in column col (not strict)
    upper_bound : upper bound of feature in column col (not strict)
    col : the column we are checking
    remove: says whether to remove the rows or not 

    Returns
    -------
    The rows that do not pass our check and the (updated) data

    '''
    problems = []
    
    for i in range(len(data[:,0])):
        if data[i, col] <= lower_bound or data[i,col] >= upper_bound:
            problems.append(i)
    
    if remove == True: 
        for i in range(len(problems)):
            np.delete(data, problems[i], 0)
    
    return problems, data 
        
    


