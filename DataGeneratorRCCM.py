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
    in column col given their severity (note the severity is prespecified) OR 
    a negative number specifying which normal distribution to use. 

    Returns
    -------
    A matrix of cases where each row is an individual 
    and each column is a feature.  

    '''
    
    # we traverse through the matrix columns
    for i in range(len(cases[:,0])):
        # fills normal distributed features
        
        # Not severe (mild)
        if prob == -1:
            cases[i,col] = np.random.normal(65.8, 9.7, 1)
        elif prob == -2:  
            cases[i,col] = np.random.normal(7.8,6.7, 1)
        elif prob == -3:  
            cases[i,col] = np.random.normal(1.3,0.6, 1)
        elif prob == -4:  
            cases[i,col] = np.random.normal(50.8,19.9, 1)
        elif prob == -5:  
            cases[i,col] = np.random.normal(36.1,12.7, 1)  
        
        # Severe
        elif prob == -1.1: 
            cases[i,col] = np.random.normal(65.1,10.5, 1)
        elif prob == -2.1:  
            cases[i,col] = np.random.normal(6.4, 4.9, 1)
        elif prob == -3.1:  
            cases[i,col] = np.random.normal(1.4, 0.6, 1)
        elif prob == -4.1:  
            cases[i,col] = np.random.normal(62.1,17.7, 1)
        elif prob == -5.1:  
            cases[i,col] = np.random.normal(47.9,9.6, 1) 
        
        else: # These are the indicator features
            rand = rnd.random()
            if rand <= prob:
                cases[i,col] = 1
            else:
                cases[i,col] = 0
        
    return cases

    
# Number of cases for each severity :
mild = 10
severe = 10

# Number of features: 
n = 10

#############################
# RCCM Data Set
#############################

# Probabilities of having the feature given the severity 
# Severe
female_s = 0.531531532
white_s = 0.932432432
retired_s = 0.527027027
bronchitis_s = 0.310344828
smoker_s = 0.31981982
# Mild
female = 0.515957447
white = 0.882978723
retired = 0.585106383
bronchitis = 0.271276596
smoker = 0.308510638

# Probability matrix for feature bases on severity:
# prob[i,j] will be the probability of having feature j given you have severity i
# If prob[i] is negative, then we use a gaussian distribution:
    ### Mild Cases
    # -1: age (mean, standard deviation) = (65.8,9.7)
    # -2: COPD diagnosis year (mean, standard deviation) = (7.8,6.7)
    # -3: FEV_1, L (mean, standard deviation) = (1.3,0.6)
    # -4: SGRQ-C Total (mean, standard deviation) = (50.8,19.9)
    # -5: EXACT scores day 1, Total (mean, standard deviation) = (36.1,12.7) 
    ### Severe Cases
    # -1.1: age (mean, standard deviation) = (65.1,10.5)
    # -2.1: COPD diagnosis year (mean, standard deviation) = (6.4, 4.9) 
    # -3.1: FEV_1, L (mean, standard deviation) = (1.4, 0.6)
    # -4.1: SGRQ-C Total (mean, standard deviation) = (62.1,17.7)
    # -5.1: EXACT scores day 1, Total (mean, standard deviation) = (47.9,9.6) 
         
prob = np.array([
    [female, white, retired, bronchitis, smoker, -1, -2, -3, -4, -5],
    [female_s, white_s, retired_s, bronchitis_s, smoker_s, -1.1, -2.1, -3.1, -4.1, -5.1]
    ])

######################################################################



# We generate a matrix for each severity type:
    # Each row is an individual
    # Each column specifies if the feature is present or not (binary)

# Here we generate the mild cases set
mild_cases = np.zeros((mild, n))
for i in range(n):
    generate_data(mild_cases, i, prob[0,i])

    
# Here we generate the severe cases set
severe_cases = np.zeros((severe, n))
for i in range(n):
    generate_data(severe_cases, i, prob[1,i])


print("Mild Cases:")
print(mild_cases)

print("Severe Cases:")
print(severe_cases)





