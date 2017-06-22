# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

# This is the improved version! We add a hint for each word
# which the user can ask to see if they are stuck. This reduces
# their score. 

import random

# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
HINTS = ("The language you are programming in.", "The type of puzzle you are playing.",
         "The opposite of difficult.", "The opposite of easy.", "The A in Q&A",
         "A metal Glockenspiel")

# we want to pick a random number so that we can pick both a
# word and its associated hint
randomPick =(random.randint(0,(len(WORDS))-1))

word = WORDS[randomPick]
hint = HINTS[randomPick]

# create a variable to use later to see if the guess is correct
correct = word

# lets say you start on 10 and every time you make an incorrect
# guess or take a hint we knock one off
score = 10

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








        



