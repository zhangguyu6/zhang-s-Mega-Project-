#Coin Flip Simulation
import random
def coin_Flip(time):
    count1 = 0
    count2 = 0
    for i in range(1000):
        k = random.randint(1, 2)
        if k == 1:
            count1 += 1
        else:
            count2 += 1
    return 'the number of tails is %d, the number of tails and heads is %d'%(count1,count2)



