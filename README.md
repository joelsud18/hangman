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

- check_guess() which checks whether the guess is in the word
- ask_for_input() which asks the user for an input, verifies it is a single alphabetical character and then calls check_guess().