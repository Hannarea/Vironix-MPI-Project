# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 14:46:20 2021

@author: hreed
"""
import numpy as np



# Number of cases for each severity :
mild = 10
moderate = 10
high = 10

# Number of features:
n=5

# Probability for feature bases on severity:



# We generate a matrix for each severity type:
    # Each row is an individual
    # Each column specifies if the feature is present or not (binary)
mild_cases = np.zeros((mild, n))
moderate_cases = np.zeros((moderate, n))
high_cases = np.zeros((high, n))


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
        
