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
        if prob == -1.1:  
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

# Number of features we are considering
n = 15

#################
# Parameters sets
#################

############ Thorax ############
# Severe cases
female_s = 0.2
male_s = 0.80
never_smoke_s = 0.129411765
ex_smoker_s = 0.494117647
smoker_s = 0.376470588
wheezing_s = 0.894117647
congestion_s = 0.494117647
rhinorrhea_s = 0.388235294
sore_throat_s = 0.223529412
sputum_s = 0.576470588
fever_s = 0.164705882
headache_s = 0.317647059
muscle_pain_s = 0.188235294
hoarse_s = 0.4
steroids_preadmission_s = 0.576470588

# Not Severe cases
female = 0.095238095
male = 1-female
never_smoke = 0.1666666667
ex_smoker = 0.547619048
smoker = 0.285714286
wheezing = 0.523809524
congestion = 0.214285714
rhinorrhea = 0.238095238
sore_throat = 0.023809524
sputum = 0
fever = 0.095238095
headache = 0.023809524
muscle_pain = 0.30952381
hoarse = 0.30952381
steroids_preadmission = 0.547619048

# Probability matrix for feature bases on severity:
# prob[i,j] will be the probability of having feature j given you have severity i
prob = np.array([
    [female, male, never_smoke, ex_smoker, smoker, wheezing, congestion, rhinorrhea, sore_throat, sputum, fever, headache, muscle_pain, hoarse, steroids_preadmission],
    [female_s, male_s, never_smoke_s, ex_smoker_s, smoker_s, wheezing_s, congestion_s, rhinorrhea_s, sore_throat_s, sputum_s, fever_s, headache_s, muscle_pain_s, hoarse_s, steroids_preadmission_s]
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





