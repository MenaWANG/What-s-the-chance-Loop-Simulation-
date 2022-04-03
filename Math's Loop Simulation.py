import random
from random import randint
list = [1, 2, 3]
truetotal = 0 # to count the total number of sucesses
falsetotal = 0 # to count the total number of failure
for i in range(10000): 
    trueorfalse = []
    random = randint(1, 3) 
    for i in list:
        trueorfalse.append(i == random)
    trueorfalse.pop() 
    trueorfalse.remove(False) # the judge takes one false number away
    if trueorfalse[0] == True: 
        truetotal += 1
    else:
        falsetotal += 1
print('The percentage of success is ', truetotal/(truetotal+falsetotal)*100)
