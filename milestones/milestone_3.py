from milestone_2 import word, word_list

def check_guess(guess): # This function checks if a character is in the selected word.
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
    guess.lower()

def ask_for_input(): #This function asks for an input, validates it is a single alphabetical character and then calls the check guess function.
    while True:
        guess = input("Please enter a single letter: ") # Asks user to input a single alphabetical letter.
        validate_guess_is_alphabetical = guess.isalpha()
        if validate_guess_is_alphabetical == True and len(guess) == 1: # Checks to see that the guess is a) alphabetical and b) a single letter.
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    
    guess.lower() #converts character to lower case.

    check_guess(guess)

ask_for_input()


