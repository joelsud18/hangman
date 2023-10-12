# Hangman

This is an Ai Core project. Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess the word by providing character guesses!

## Files

This repository contains the following files:
### milestone_2.py:
 This defines the variables used within the game. This includes:

 - the word list containing all the words the computer chooses from.
 - the word selector.

### milestone_3.py:
This imports the word from milsetone_2.py and defines the following functions:

- check_guess() which checks whether the guess is in the word.
- ask_for_input() which asks the user for an input, verifies it is a single alphabetical character and then calls check_guess().

### milestone_4.py:
This takes the code from the previous milestones and develops the functions as methods under a 'Hangman' class, This file contains the following:

- Hangman class is defined.
- '__init__()' method is defined with following attributes:
    - self.word_list - list of words for computer to choose from.
    - self.num_lives - number of lives the user has.
    - self.word - a randomly selected word from the word_list.
    - self.word_guessed - a list containing how many characters have been guessed correctly from the word.
    - self.num_letters - the number of letters in the selected word.
    - self.list_of_guesses - every character that the user has guessed.
    - self.total_num_guesses - the total number of guesses made by the user.
- 'check_guess()' method is defined which:
    - makes the guessed character lower case.
    - if the guess is in the word it notifies the user and adds the letter to the words_guessed list.
    - if the guess is not in the word, the user is notified and a life is taken away from num_lives.
- 'ask_for_input' method is defined which:
    - asks the user for an input.
    - verifies whether the input is a single alphabetical character that has not already been guessed. If it is, they are asked for anotehr input.
    - if it is a valid input it is added to the list_of_guesses and passed through to the check_guess() method.