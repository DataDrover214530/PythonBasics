# Guess My Number v3
#
# I use my D&D dice to  pick a random number between 1 and 100 and the
# computer tries to guess it. I give feedback of higher or lower until
# the computer guesses right. The computer guesses by rolling a random
# number and modifies its roll based on my clues

import random  

upperbound = 100
lowerbound = 1

print("\tHey Hal, Welcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

#Computer generates initial guess as a random number between 1-100
guess = random.randint(lowerbound, upperbound)

while feedback != "Y":
    print ("\nMy guess is", guess)
    feedback = input("\nPlease type 'H' if your number is higher. 'L' if it is lower or 'Y' if I got it right\n")
    
    if feedback=="H":
        lowerbound = guess + 1
        guess = random.randint(lowerbound, upperbound)
    if feedback=="L":
        upperbound = guess - 1
        guess = random.randint(lowerbound, upperbound)
    if feedback=="Y":
        pass
    else:
        print("\nI'm sorry Dave, I need you to type H, L or Y. Please try again\n")
    
    
        
print("\nHal says, 'In your face Dave I guessed your stupid number so out the airlock you go!'")
  
input("\n\nPress the enter key to exit.")
