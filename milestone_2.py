import random

word_list = ['mango', 'strawberry', 'raspberry', 'orange', 'grapes']

word = random.choice(word_list)

guess = input("Please enter a single letter: ")
if len(guess)=1:
    print("Good Guess!")
else:
    print("Oops! That is not a valid input.")

