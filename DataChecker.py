# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 14:20:47 2021

@author: hreed
"""

import numpy as np

def check_range(data, lower_bound, upper_bound, col, remove = False):
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
        
    
    
    

def check_mild(data, col1, col2, lim, delete = False):
    '''
    Checks that the data is reasonable, indended to deal with the mild cases 
    (we don't want too many features to be present) 

    Parameters
    ----------
    data : matrix of cases, rows are individuals and columns are features
    col1 : beginning column to check 
    col2 : end column to check 
    lim : the number of features that can be indicated
    delete : indicates whether to delete the rows that are deemed no reasonable

    Returns
    -------
    The (updated) array of data and the number of bad cases there were/are

    '''
    data_bad = 0
    
    for i in range(len(data[:,0])):
        if sum(data[i, col1:col2]) >= lim:
            if delete == True:
                data = np.delete(data, i, 0)
            data_bad += 1
    
    return data, data_bad

    


