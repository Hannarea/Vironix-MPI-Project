# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 14:46:20 2021

@author: hreed
"""
import numpy as np
import random as rnd



def generate_data(cases, col, prob):
    '''
    
    Parameters
    ----------
    cases : A matrix of cases where each row is an individual 
    and each column is a feature 
    col : The column of the feature we are generating values for
    prob : the probability that an individual has the feature represented 
    in column col given their severity (note the severity is prespecified)

    Returns
    -------
    A matrix of cases where each row is an individual 
    and each column is a feature.  

    '''
    
    # we traverse through the matrix columns
    for i in range(len(cases[:,0])):
        # Generate a random number between 0 and 1
        rand = rnd.random()
        if rand <= prob:
            cases[i,col] = 1
        else:
            cases[i,col] = 0
    
    return cases



 
##########################
# Example of use 
##########################    
    
# Number of cases for each severity :
mild = 10
moderate = 10
high = 10

# Number of features:
n=2

# Probability for feature bases on severity:
test1 = .2
test2 = .9

# We generate a matrix for each severity type:
    # Each row is an individual
    # Each column specifies if the feature is present or not (binary)
mild_cases = np.zeros((mild, n))
moderate_cases = np.zeros((moderate, n))
high_cases = np.zeros((high, n))



mild_cases = generate_data(mild_cases, 0, test1)
mild_cases = generate_data(mild_cases, 1, test2)

print(mild_cases)



