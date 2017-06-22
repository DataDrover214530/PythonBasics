# Progam which defines 5 posible "fortune cookie" cookies and then selects one at random

import random

fortune1 ="You will find a penny on the floor"
fortune2 ="The rain in Spain falls mainly on the plain so be sure to take an umbrella"
fortune3 ="Wise men say only fools rush in"
fortune4 ="Don't be evil"
fortune5 ="Always mulligan on the curve and you will find success"

print("** Roll up roll up and I will tell your fortune!... **\n \
**************************************************\n")

rollRandInt = random.randint(1,5)
rollRandRange = random.randrange(5)+1

if rollRandInt == 1:
    RandintFortune = fortune1
elif rollRandInt == 2:
    RandintFortune = fortune2
elif rollRandInt == 3:
    RandintFortune == fortune3
elif rollRandInt == 4:
    RandintFortune = fortune4
elif rollRandInt == 5:
    RandintFortune = fortune5
else:
    RandintFortune = "You have no fortune, you unfortunate soul"


if rollRandRange == 1:
    RandRangeFortune = fortune1
elif rollRandRange == 2:
    RandRangeFortune = fortune2
elif rollRandRange == 3:
    RandRangeFortune = fortune3
elif rollRandRange == 4:
    RandRangeFortune = fortune4
elif rollRandRange == 5:
    RandRangeFortune = fortune5
else:
    RandRangeFortune = "You have no fortune, you unfortunate soul"


print("\nBehold your fortune as selected by the Oracle Randint\n '", RandintFortune, "'\nMay it serve you well.")

print("\nNow behold your fortune as selected by the Oracle Randrange\n '", RandRangeFortune, "'\nMay it too serve you well.")

input("\n\nPress the enter key to exit.")

