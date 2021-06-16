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
                
    if prob == -1: # from RCCM paper, age_s, mean = 65.1, standard deviation = 10.5
        for i in range(len(cases[:,0])):
            # Generate a random age
            age = np.random.normal(65.1,10.5, 1)
            # Categorize the age
            if age < 50: 
                cases[i,col] = 0
            elif age < 60:
                cases[i,col] = 1
            elif age < 70:
                cases[i,col] = 2
            elif age < 80:
                cases[i,col] = 3
            else:
                cases[i,col] = 4
                
    elif prob == -1.1: # from RCCM paper, age, mean = 65.8, standard deviation = 9.7    
        for i in range(len(cases[:,0])):
            # Generate a random age
            age = np.random.normal(65.8,9.7, 1)
            # Categorize the age
            if age < 50: 
                cases[i,col] = 0
            elif age < 60:
                cases[i,col] = 1
            elif age < 70:
                cases[i,col] = 2
            elif age < 80:
                cases[i,col] = 3
            else:
                cases[i,col] = 4
        
    elif prob == -2: # from RCCM paper, previous exacerbation_s, mean = 2.2, standard deviation = 2.1
        for i in range(len(cases[:,0])):
            # Generate a random age
            pre_ex = np.random.normal(2.2,2.1, 1)
            # Categorize the age
            if pre_ex < 0.5: 
                cases[i,col] = 0
            elif pre_ex < 1.5:
                cases[i,col] = 1
            elif pre_ex < 2.5:
                cases[i,col] = 2
            elif pre_ex < 3.5:
                cases[i,col] = 3
            else:
                cases[i,col] = 4
        
    elif prob == -2.1: # from RCCM paper, previous exacerbation, mean = 1.3, standard deviation = 1.2
        for i in range(len(cases[:,0])):
            # Generate a random age
            pre_ex = np.random.normal(1.3,1.2, 1)
            # Categorize the age
            if pre_ex < 0.5: 
                cases[i,col] = 0
            elif pre_ex < 1.5:
                cases[i,col] = 1
            elif pre_ex < 2.5:
                cases[i,col] = 2
            elif pre_ex < 3.5:
                cases[i,col] = 3
            else:
                cases[i,col] = 4
        
    else:
        for i in range(len(cases[:,0])):
            rand = rnd.random()
            if rand <= prob:
                cases[i,col] = 1
            else:
                cases[i,col] = 0
        
    return cases


    
# Number of cases for each severity :
mild = 50
severe = 50

# Number of features we are considering
n = 10

#################
# Parameters sets
#################

############ Thorax ############

# Probabilities of having the feature given the severity 
# Severe cases
age_s = -1
previous_exacerbation_s = -2
female_s = 0.2
smoker_s = 0.376470588
wheezing_s = 0.894117647
congestion_s = 0.494117647
rhinorrhea_s = 0.388235294
sore_throat_s = 0.223529412
sputum_s = 0.576470588
headache_s = 0.317647059
# Not Severe cases
age = -1.1
previous_exacerbation = -2.1
female = 0.095238095
smoker = 0.285714286
wheezing = 0.523809524
congestion = 0.214285714
rhinorrhea = 0.238095238
sore_throat = 0.023809524
sputum = 0
headache = 0.023809524

# Probability matrix for feature bases on severity:
# prob[i,j] will be the probability of having feature j given you have severity i
prob = np.array([
    [age, previous_exacerbation, female, smoker, wheezing, congestion, rhinorrhea, sore_throat, sputum, headache],
    [age_s, previous_exacerbation_s, female_s, smoker_s, wheezing_s, congestion_s, rhinorrhea_s, sore_throat_s, sputum_s, headache_s]
    ])


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





