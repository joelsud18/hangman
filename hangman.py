import random


class Hangman:

    '''
    This class is used to define the game hangman.

    Attributes:
        word_list (list): The list of words the computer selects a word at random from.
        num_lives (int): The number of lives the user starts with.
    '''

    def __init__(self, word_list, num_lives = 5):

        '''
        See help(Hangman) for accurate signature.
        '''

        self.word_list = word_list
        self.num_lives = num_lives

        self.word = random.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(self.word)
        self.list_of_guesses = []
        self.total_num_guesses = 0

    def check_guess(self, guess):
        
        '''
        This method is used to check whether the letter guessed by the user is in the selected word. if not then it takes a life away from the user.

        Args:
            guess (string): This is the letter input from the user.
        '''

        guess = guess.lower()
        if guess in self.word:
            print(f"\nGood guess! {guess} is in the word. \n")
            index = 0
            for letter in self.word:
                if letter == guess:
                    self.word_guessed[index] = guess
                    self.num_letters -= 1
                index += 1
            print(f"{self.word_guessed} \n")
        else:
            self.num_lives -= 1
            print(f"\nSorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left! \n")
            print(f"{self.word_guessed} \n")

    def ask_for_input(self):

        '''
        This method asks the user for an input and checks that the letter is:
            1. a single character
            2. alphabetical
            3. not been guessed before
        if the input is valid then it passes it as an argument into the check_guess() method.
        '''

        while True:
            if self.num_letters == 0 or self.num_lives == 0:
                break 
            guess = input("Please enter a single letter: ")
            validate_guess_is_alphabetical = guess.isalpha()
            if validate_guess_is_alphabetical == False or len(guess) != 1:
                print("\nInvalid letter. Please, enter a single alphabetical character. \n")
            elif guess in self.list_of_guesses:
                print("\nYou already tried that letter. \n")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                self.total_num_guesses += 1

def play_game(word_list):

    '''
    This function defines the logic of the game by taking in a word list and creating an instance of the hangman class and calling both of its methods. 

    Args:
        word_list (list): the list of words the game is played from.
    '''

    num_lives = 5
    game = Hangman(word_list, num_lives)
    print(f"\n Guess the word: \n{game.word_guessed} \n")
    while True:
        game.ask_for_input()
        if game.num_lives == 0:
            print(f"You lost!\nThe word was: {game.word}")
            break
        else:
            print(f"Congatulations! You won the game!\nthe word was: {game.word}")
            print(f"it took you {game.total_num_guesses} guesses to win!\n")
            break

word_list = ["apple", "banana", "carrot", "elephant", "flower",
    "guitar", "jacket", "kite", "lion", "mountain",
    "notebook", "ocean", "piano", "quilt", "sailboat",
    "umbrella", "violin", "zebra", "airplane", "beach",
    "coffee", "dolphin", "eleven", "giraffe", "hamster",
    "island", "jungle", "kingdom", "leopard", "mango",
    "pineapple", "tiger", "sunflower", "waterfall", "whale",
    "cucumber", "penguin", "chocolate", "laptop", "sunrise",
    "butterfly", "giraffe", "river", "mountain", "desert"]

if __name__ == "__main__":
    play_game(word_list)
