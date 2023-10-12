import random

class Hangman:

    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives

        self.word = random.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(self.word)
        self.list_of_guesses = []
        self.total_num_guesses = 0

    def check_guess(self, guess): # This function checks if a character is in the selected word.
        
        guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            index = 0
            for letter in self.word:
                if letter == guess:
                    self.word_guessed[index] = guess
                    self.num_letters -= 1
                index += 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} left!")

    def ask_for_input(self): #This function asks for an input, validates it is a single alphabetical character and then calls the check guess function.
        while True:
            guess = input("Please enter a single letter: ")
            validate_guess_is_alphabetical = guess.isalpha()
            if validate_guess_is_alphabetical == False or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter.")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                self.total_num_guesses += 1

word_list = ['mango', 'apple', 'strawberry', 'raspberry', 'kiwi']