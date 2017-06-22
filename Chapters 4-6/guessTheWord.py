# Guess that Word!
#
# The computer picks a random word and you have to guess it!

# You get to guess at 5 letter in the word, the computer will
# tell you yes or no. After you have 5 hint letters you have to
# guess.

import random

# create a sequence of words to choose from
WORDS = ("python", "jumble", "easypeasy", "difficult", "answer", "xylophone")


# pick one word randomly from the sequence
word = random.choice(WORDS)



# create a variable to use later to see if the guess is correct
correct = word



# create a jumbled version of the word
jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# start the game
print(
"""
           Welcome to Word Jumble!
        
   Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
"""
)



print("The jumble is:", jumble)

guess = input("\nYour guess: ")
while guess != correct and guess != "":
    print("Sorry, that's not it.")
    score -= 1
    guess = input("Try again or hit ? for a hint: ")

    if guess == "?":
        print(hint)
        score -= 1
        guess = input("Your guess: ")
    
if guess == correct:
    print("That's it!  You guessed it!\nYour score was ", score)

print("Thanks for playing.")

input("\n\nPress the enter key to exit.")








        



