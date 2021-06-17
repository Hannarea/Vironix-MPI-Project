# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 15:11:58 2021

@author: hreed
"""
import numpy as np
import matplotlib.pyplot as plt

file = open("eh.csv")

arr = np.loadtxt(file, delimiter=",")

mild = []
severe = []
for i in range(1000):
    if arr[i,10] == 0 and len(mild)<479:
        mild.append(arr[i])
        
    if arr[i,10] == 1:
        severe.append(arr[i])

mild_cases = np.array(mild)
severe_cases = np.array(severe)
  
print(len(mild))
print(len(severe))
mild = len(mild)
severe = len(severe)


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
plt.title("Multivariate Age Distributions")
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

for i in range(len(mild_cases[:,3])): # previous exacerbation is the second column 
    if mild_cases[i,3] == 0:
        pe_group0 += 1
    if mild_cases[i,3] == 1:
        pe_group1 += 1
    if mild_cases[i,3] == 2:
        pe_group2 += 1
    if mild_cases[i,3] == 3:
        pe_group3 += 1
    if mild_cases[i,3] == 4:
        pe_group4 += 1


# We want to plot the age distribution for the severe cases: 
pe_s_group0 = 0
pe_s_group1 = 0
pe_s_group2 = 0
pe_s_group3 = 0
pe_s_group4 = 0  
pe_s_group5 = 0 

for i in range(len(severe_cases[:,0])): # previous exacerbation is the second column 
    if severe_cases[i,3] == 0:
        pe_s_group0 += 1
    if severe_cases[i,3] == 1:
        pe_s_group1 += 1
    if severe_cases[i,3] == 2:
        pe_s_group2 += 1
    if severe_cases[i,3] == 3:
        pe_s_group3 += 1
    if severe_cases[i,3] == 4:
        pe_s_group4 += 1

data = [[pe_group0, pe_group1, pe_group2, pe_group3, pe_group4],
[pe_s_group0, pe_s_group1, pe_s_group2, pe_s_group3, pe_s_group4]]
X = np.arange(5)
fig = plt.figure()
plt.bar(X + 0.00, data[0], color = 'b', width = 0.25, label = "Mild")
plt.bar(X + 0.25, data[1], color = 'r', width = 0.25, label = "Severe")
plt.title("Multivariate Previous Exacerbation Distributions")
plt.xlabel("Previous Exacerbations")
plt.ylabel("Individual Count")
plt.legend()
plt.show()


###########################################################################
# Sex
###########################################################################

female = 0
female_s = 0

for i in range(len(mild_cases[:,1])):
    if mild_cases[i, 1] == 1:
        female += 1
for i in range(len(severe_cases[:,1])):
    if severe_cases[i,1] == 1:
        female_s += 1
        
        
data = [[mild - female, female],
[severe - female_s, female_s]]
X = np.arange(2)
fig = plt.figure()
plt.bar(X + 0.00, data[0], color = 'b', width = 0.25, label = "Mild")
plt.bar(X + 0.25, data[1], color = 'r', width = 0.25, label = "Severe")
plt.xticks([0, 1])
plt.title("Multivariate Sex Distributions")
plt.xlabel("Sex")
plt.ylabel("Individual Count")
plt.legend()
plt.show()



########################################
# Smoker
########################################

count = 0
count_s = 0

for i in range(len(mild_cases[:,2])):
    if mild_cases[i, 2] == 1:
        count += 1
for i in range(len(severe_cases[:,2])):
    if severe_cases[i,2] == 1:
        count_s += 1
        
        
data = [[mild - count, count],
[severe - count_s, count_s]]
X = np.arange(2)
fig = plt.figure()
plt.bar(X + 0.00, data[0], color = 'b', width = 0.25, label = "Mild")
plt.bar(X + 0.25, data[1], color = 'r', width = 0.25, label = "Severe")
plt.xticks([0, 1])
plt.title("Multivariate Smoker Distributions")
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
plt.title("Multivariate Wheezing Distributions")
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
plt.title("Multivariate Congestion Distributions")
plt.xlabel("Congestion")
plt.ylabel("Individual Count")
plt.legend()
plt.show()


########################################
# Rhinorrhea
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
plt.title("Multivariate Rhinorrhea Distributions")
plt.xlabel("Rhinorrhea")
plt.ylabel("Individual Count")
plt.legend()
plt.show()


########################################
# Sore Throat
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
plt.title("Multivariate Sore Throat Distributions")
plt.xlabel("Sore Throat")
plt.ylabel("Individual Count")
plt.legend()
plt.show()


########################################
# Sputum
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
plt.title("Multivariate Sputum Distributions")
plt.xlabel("Sputum")
plt.ylabel("Individual Count")
plt.legend()
plt.show()


########################################
# Headache
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
plt.title("Multivariate Headache Distributions")
plt.xlabel("Headache")
plt.ylabel("Individual Count")
plt.legend()
plt.show()

