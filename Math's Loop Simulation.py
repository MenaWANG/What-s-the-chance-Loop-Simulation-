import random
from random import randint
list = [1, 2, 3]
truetotal = 0 # count the times of picking the TRUE number
falsetotal = 0 # count the times of picking the FALSE number
for i in range(10000): # try the strategy 10,000 times
    trueorfalse = [] 
    random = randint(1, 3) # bring the randomness in: one in three is the TRUE number
    for i in list:
        trueorfalse.append(i == random)
    trueorfalse.pop() # remove the number I picked
    trueorfalse.remove(False) # the judge remove the FALSE number left
    if trueorfalse[0] == True: # if the number left is TRUE, then one more success
        truetotal += 1
    else: # else one more failure
        falsetotal += 1
print('The chance of success if I always choose the number left by the judge: ', truetotal/(truetotal+falsetotal)*100)
