# Progam which simulates a coin flip 100 times and then outputs the results

import random


print("** Flippin' a coin to see what's what!... **\n \
**************************************************\n")
heads=0
tails=0

for i in range(100):
    coinflip = random.randint(0,1)
    if coinflip == 0:
        heads+=1
    else:
        tails+=1



print("\nHeads came up", heads, "times")
print("\nTails came up", tails, "times")

input("\n\nPress the enter key to exit.")

