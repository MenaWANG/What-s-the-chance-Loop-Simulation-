import random
from random import randint
list = [1, 2, 3]
truenumber = 0
falsenumber = 0
for i in range(3000):
    trueorfalse = []
    random = randint(1, 3)
    for i in list:
        trueorfalse.append(i == random)
    trueorfalse.pop()
    trueorfalse.remove(False)
    if trueorfalse[0] == True:
        truenumber += 1
    else:
        falsenumber += 1
print(truenumber/(truenumber+falsenumber)*100)