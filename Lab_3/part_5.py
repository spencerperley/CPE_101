import random as rand
heads = 0
tails = 0
numFlips =200000
for i in range(0,numFlips):
    flip = rand.random()
    if flip >= .5 :
        # print("Heads!")
        heads+=1
        
    else:
        # print("Tails!")
        tails+=1
        
print(f"After 150 flips there were {heads} heads and {tails} tails \n The probablitity of heads is {heads/numFlips} \n the probalbillit of tails is {tails/numFlips}")