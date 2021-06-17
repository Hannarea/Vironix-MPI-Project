# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 11:12:58 2021

@author: hreed
"""

# Plots of some data

import numpy as np
import matplotlib.pyplot as plt
from DataGeneratorThorax import generate_data

def fun(x, mu, sig):
    return 1/(sig*np.sqrt(2*np.pi))*np.exp(-1/2*((x-mu)/sig)**2)

x = np.linspace(0,100, 100)

age_s = np.zeros(len(x))
age = np.zeros(len(x))
for i in range(len(x)):
    age_s[i] = fun(x[i], 65.1, 10.5)
    age[i] = fun(x[i], 65.8, 9.7)
    
    
plt.plot(x,age_s, 'r', label = "Severe")
plt.plot(x, age, 'b', label = "Mild")
plt.title("Age Distributions")
plt.xlabel("Age")
plt.ylabel("Probability")
plt.legend()
plt.show()


x = np.linspace(0, 6, 100)

preex_s = np.zeros(len(x))
preex = np.zeros(len(x))
for i in range(len(x)):
    preex_s[i] = fun(x[i], 2.2, 2.1)
    preex[i] = fun(x[i], 1.3, 1.2)

plt.plot(x,preex_s, 'r', label = "Severe")
plt.plot(x, preex, 'b', label = "Mild")
plt.title("Previous Exacerbations Distributions")
plt.xlabel("Previous Exacerbations")
plt.ylabel("Probability")
plt.legend()
plt.show()


### Parameters ######################
############ From Thorax ############
# Probabilities of having the feature given the severity 
# Severe cases
age_s = -1 # reference in function
previous_exacerbation_s = -2 # reference in function
female_s = 0.2
smoker_s = 0.376470588
wheezing_s = 0.894117647
congestion_s = 0.494117647
rhinorrhea_s = 0.388235294
sore_throat_s = 0.223529412
sputum_s = 0.576470588
headache_s = 0.317647059
# Not Severe cases
age = -1.1 # reference in function
previous_exacerbation = -2.1 # reference in function
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

###########################################################################
       
#Generating the data
n = 10
mild = 1000
severe = 1000
    
# Here we generate the mild cases set
mild_cases = np.zeros((mild, n))
for i in range(n):
    generate_data(mild_cases, i, prob[0,i])

    
# Here we generate the severe cases set
severe_cases = np.zeros((severe, n))
for i in range(n):
    generate_data(severe_cases, i, prob[1,i])








##########################################################
# Age Distributions
##########################################################
# We want to plot the age distribution for the mild cases: 
age_group0 = 0
age_group1 = 0
age_group2 = 0
age_group3 = 0
age_group4 = 0  
age_group5 = 0 

for i in range(len(mild_cases[:,0])): # age is the first column 
    if mild_cases[i,0] == 0:
        age_group0 += 1
    if mild_cases[i,0] == 1:
        age_group1 += 1
    if mild_cases[i,0] == 2:
        age_group2 += 1
    if mild_cases[i,0] == 3:
        age_group3 += 1
    if mild_cases[i,0] == 4:
        age_group4 += 1


# We want to plot the age distribution for the severe cases: 
age_s_group0 = 0
age_s_group1 = 0
age_s_group2 = 0
age_s_group3 = 0
age_s_group4 = 0  
age_s_group5 = 0 

for i in range(len(severe_cases[:,0])): # age is the first column 
    if severe_cases[i,0] == 0:
        age_s_group0 += 1
    if severe_cases[i,0] == 1:
        age_s_group1 += 1
    if severe_cases[i,0] == 2:
        age_s_group2 += 1
    if severe_cases[i,0] == 3:
        age_s_group3 += 1
    if severe_cases[i,0] == 4:
        age_s_group4 += 1

data = [[age_group0, age_group1, age_group2, age_group3, age_group4],
[age_s_group0, age_s_group1, age_s_group2, age_s_group3, age_s_group4]]
X = np.arange(5)
fig = plt.figure()
plt.bar(X + 0.00, data[0], color = 'b', width = 0.25, label = "Mild")
plt.bar(X + 0.25, data[1], color = 'r', width = 0.25, label = "Severe")
plt.title("Age Distributions")
plt.xlabel("Age Groups")
plt.ylabel("Individual Count")
plt.legend()
plt.show()

#######################################################################


#####################################################################
# Previous Exacerbation 
#####################################################################
# We want to plot the age distribution for the mild cases: 
pe_group0 = 0
pe_group1 = 0
pe_group2 = 0
pe_group3 = 0
pe_group4 = 0  
pe_group5 = 0 

for i in range(len(mild_cases[:,1])): # previous exacerbation is the second column 
    if mild_cases[i,1] == 0:
        pe_group0 += 1
    if mild_cases[i,1] == 1:
        pe_group1 += 1
    if mild_cases[i,1] == 2:
        pe_group2 += 1
    if mild_cases[i,1] == 3:
        pe_group3 += 1
    if mild_cases[i,1] == 4:
        pe_group4 += 1


# We want to plot the age distribution for the severe cases: 
pe_s_group0 = 0
pe_s_group1 = 0
pe_s_group2 = 0
pe_s_group3 = 0
pe_s_group4 = 0  
pe_s_group5 = 0 

for i in range(len(severe_cases[:,0])): # previous exacerbation is the second column 
    if severe_cases[i,1] == 0:
        pe_s_group0 += 1
    if severe_cases[i,1] == 1:
        pe_s_group1 += 1
    if severe_cases[i,1] == 2:
        pe_s_group2 += 1
    if severe_cases[i,1] == 3:
        pe_s_group3 += 1
    if severe_cases[i,1] == 4:
        pe_s_group4 += 1

data = [[pe_group0, pe_group1, pe_group2, pe_group3, pe_group4],
[pe_s_group0, pe_s_group1, pe_s_group2, pe_s_group3, pe_s_group4]]
X = np.arange(5)
fig = plt.figure()
plt.bar(X + 0.00, data[0], color = 'b', width = 0.25, label = "Mild")
plt.bar(X + 0.25, data[1], color = 'r', width = 0.25, label = "Severe")
plt.title("Previous Exacerbation Distributions")
plt.xlabel("Previous Exacerbations")
plt.ylabel("Individual Count")
plt.legend()
plt.show()


###########################################################################
# Sex
###########################################################################

female = 0
female_s = 0

for i in range(len(mild_cases[:,2])):
    if mild_cases[i, 2] == 1:
        female += 1
for i in range(len(severe_cases[:,2])):
    if severe_cases[i,2] == 1:
        female_s += 1
        
        
data = [[mild - female, female],
[severe - female_s, female_s]]
X = np.arange(2)
fig = plt.figure()
plt.bar(X + 0.00, data[0], color = 'b', width = 0.25, label = "Mild")
plt.bar(X + 0.25, data[1], color = 'r', width = 0.25, label = "Severe")
plt.xticks([0, 1])
plt.title("Sex Distributions")
plt.xlabel("Sex")
plt.ylabel("Individual Count")
plt.legend()
plt.show()



########################################
# Smoker
########################################

count = 0
count_s = 0

for i in range(len(mild_cases[:,3])):
    if mild_cases[i, 3] == 1:
        count += 1
for i in range(len(severe_cases[:,3])):
    if severe_cases[i,3] == 1:
        count_s += 1
        
        
data = [[mild - count, count],
[severe - count_s, count_s]]
X = np.arange(2)
fig = plt.figure()
plt.bar(X + 0.00, data[0], color = 'b', width = 0.25, label = "Mild")
plt.bar(X + 0.25, data[1], color = 'r', width = 0.25, label = "Severe")
plt.xticks([0, 1])
plt.title("Smoker Distributions")
plt.xlabel("Smoker")
plt.ylabel("Individual Count")
plt.legend()
plt.show()




########################################
# Wheezing
########################################

count = 0
count_s = 0

for i in range(len(mild_cases[:,4])):
    if mild_cases[i, 4] == 1:
        count += 1
for i in range(len(severe_cases[:,4])):
    if severe_cases[i,4] == 1:
        count_s += 1
        
        
data = [[mild - count, count],
[severe - count_s, count_s]]
X = np.arange(2)
fig = plt.figure()
plt.bar(X + 0.00, data[0], color = 'b', width = 0.25, label = "Mild")
plt.bar(X + 0.25, data[1], color = 'r', width = 0.25, label = "Severe")
plt.xticks([0, 1])
plt.title("Wheezing Distributions")
plt.xlabel("Wheezing")
plt.ylabel("Individual Count")
plt.legend()
plt.show()


########################################
# Congestion
########################################

count = 0
count_s = 0

for i in range(len(mild_cases[:,5])):
    if mild_cases[i, 5] == 1:
        count += 1
for i in range(len(severe_cases[:,5])):
    if severe_cases[i,5] == 1:
        count_s += 1
        
        
data = [[mild - count, count],
[severe - count_s, count_s]]
X = np.arange(2)
fig = plt.figure()
plt.bar(X + 0.00, data[0], color = 'b', width = 0.25, label = "Mild")
plt.bar(X + 0.25, data[1], color = 'r', width = 0.25, label = "Severe")
plt.xticks([0, 1])
plt.title("Congestion Distributions")
plt.xlabel("Congestion")
plt.ylabel("Individual Count")
plt.legend()
plt.show()


########################################
# Rhinorrhea
########################################

count = 0
count_s = 0

for i in range(len(mild_cases[:,6])):
    if mild_cases[i, 6] == 1:
        count += 1
for i in range(len(severe_cases[:,6])):
    if severe_cases[i,6] == 1:
        count_s += 1
        
        
data = [[mild - count, count],
[severe - count_s, count_s]]
X = np.arange(2)
fig = plt.figure()
plt.bar(X + 0.00, data[0], color = 'b', width = 0.25, label = "Mild")
plt.bar(X + 0.25, data[1], color = 'r', width = 0.25, label = "Severe")
plt.xticks([0, 1])
plt.title("Rhinorrhea Distributions")
plt.xlabel("Rhinorrhea")
plt.ylabel("Individual Count")
plt.legend()
plt.show()


########################################
# Sore Throat
########################################

count = 0
count_s = 0

for i in range(len(mild_cases[:,7])):
    if mild_cases[i, 7] == 1:
        count += 1
for i in range(len(severe_cases[:,7])):
    if severe_cases[i,7] == 1:
        count_s += 1
        
        
data = [[mild - count, count],
[severe - count_s, count_s]]
X = np.arange(2)
fig = plt.figure()
plt.bar(X + 0.00, data[0], color = 'b', width = 0.25, label = "Mild")
plt.bar(X + 0.25, data[1], color = 'r', width = 0.25, label = "Severe")
plt.xticks([0, 1])
plt.title("Sore Throat Distributions")
plt.xlabel("Sore Throat")
plt.ylabel("Individual Count")
plt.legend()
plt.show()


########################################
# Sputum
########################################

count = 0
count_s = 0

for i in range(len(mild_cases[:,8])):
    if mild_cases[i, 8] == 1:
        count += 1
for i in range(len(severe_cases[:,8])):
    if severe_cases[i,8] == 1:
        count_s += 1
        
        
data = [[mild - count, count],
[severe - count_s, count_s]]
X = np.arange(2)
fig = plt.figure()
plt.bar(X + 0.00, data[0], color = 'b', width = 0.25, label = "Mild")
plt.bar(X + 0.25, data[1], color = 'r', width = 0.25, label = "Severe")
plt.xticks([0, 1])
plt.title("Sputum Distributions")
plt.xlabel("Sputum")
plt.ylabel("Individual Count")
plt.legend()
plt.show()


########################################
# Headache
########################################

count = 0
count_s = 0

for i in range(len(mild_cases[:,9])):
    if mild_cases[i, 9] == 1:
        count += 1
for i in range(len(severe_cases[:,9])):
    if severe_cases[i,9] == 1:
        count_s += 1
        
        
data = [[mild - count, count],
[severe - count_s, count_s]]
X = np.arange(2)
fig = plt.figure()
plt.bar(X + 0.00, data[0], color = 'b', width = 0.25, label = "Mild")
plt.bar(X + 0.25, data[1], color = 'r', width = 0.25, label = "Severe")
plt.xticks([0, 1])
plt.title("Headache Distributions")
plt.xlabel("Headache")
plt.ylabel("Individual Count")
plt.legend()
plt.show()

