import random
# This is the list of words the computer will select its word from.
word_list = ['mango', 'strawberry', 'raspberry', 'orange', 'grapes']

selected_word = random.choice(word_list) # The computer selects word at random from the list.

user_guess = input("Please enter a single letter: ") # Computer asks user to make a guess by providing a character.
# Computer will check the user guess is one character in length.
if len(user_guess) == 1:
    print("Good Guess!")
else:
    print("Oops! That is not a valid input.")