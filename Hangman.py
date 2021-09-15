import os
import os.path
from os import path
import time

WORDS_LIST = []  # Keep the words of the file in a list
HANGMAN_PHOTOS = {1: "    x-------x", 2: """    x-------x
    |
    |
    |
    |
    |""", 3: """    x-------x
    |       |
    |       0
    |
    |
    |""", 4: """    x-------x
    |       |
    |       0
    |       |
    |
    |""", 5: """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""", 6: """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""", 7: """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""}


def clear():  # Clears the screen
    os.system('cls')


def file_reader(file_path, index):
    """Reads the file, keep the words in list and checks for correct input.
    :param file_path: the path to the file
    :param index: index value
    :type file_path: str
    :type index: int
    :return: opens the file path and insert each parameter to the right way
    :rtype: bool
    """
    global WORDS_LIST
    with open(file_path, 'r') as file:
        f = file.read()
        WORDS_LIST = f.split()
    count = len(WORDS_LIST)  # Saves the amount of words
    index = int(index)  # Saves the user index to which he wants to reffer
    while not (index <= count):
        print("The index you inserted is wrong, please insert new one:")
        index = input()
        index = int(index)


def check_valid_input(letter_guessed, old_letters_guessed):
    """Checks for the validity of the input.
    :param letter_guessed: the letter guessed allready
    :param index: index value
    :type letter_guessed: char
    :type index: int
    :return: True if valid else False
    :rtype: bool
    """
    if len(letter_guessed) >= 2 or not (letter_guessed.islower()) or letter_guessed in old_letters_guessed:
        return False
    else:
        return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """Checks if the letter is allready inserted.
    :param letter_guessed: the letter the user inserted
    :param old_letters_guessed: the letters already guessed
    :type letter_guessed: char
    :type old_letters_guessed: char
    :return: True if valid else False
    :rtype: bool
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:  # If inserted allready prints the letters that was inserted until now and returns false
        print("X")
        print(" -> ".join(sorted(old_letters_guessed)))
        return False


def show_hidden_word(secret_word, old_letters_guessed):
    """If the letter is in the secret word prints it in the correct position.
    :param secret_word: the secret word in the file
    :param old_letters_guessed: the letters already guessed
    :type secret_word: char
    :type old_letters_guessed: char
    :return: place the letter in the places and reveal
    :rtype: str
    """
    print("\n")
    for letter in secret_word:
        if letter in old_letters_guessed:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    return ' '


def check_win(secret_word, old_letters_guessed):
    """The func. checks if the letter that guessed until now, if the letters match the secret word player wins
    :param secret_word: the secret word in the file
    :param old_letters_guessed: the letters already guessed
    :type secret_word: char
    :type old_letters_guessed: char
    :return: returns True if you guessed all letters
    :rtype: bool
    """
    for letters_guessed in secret_word:
        if letters_guessed in old_letters_guessed:
            continue
        else:
            return False
    return True


def choose_word(file_path, index):
    """Choose the secret word from the file by user input
    :param file_path: the path to the file
    :param index: index value
    :type file_path: str
    :type index: int
    :return: the word in index
    :rtype: str
    """
    file_string = WORDS_LIST
    word_in_place = ""
    new_list = []  # Holds the words that are not doubled
    for i in range(0, len(WORDS_LIST), 1):
        if file_string[i] in new_list:
            continue
        new_list.append(file_string[i])
    index = int(index)
    word_in_place += file_string[index]
    return word_in_place


def loser():
    # What to print when player loses
    print("""     _                     
    | |                    
    | | ___  ___  ___ _ __ 
    | |/ _ \/ __|/ _ \ '__|
    | | (_) \__ \  __/ |   
    |_|\___/|___/\___|_|   """)


def winner():
    # What to print when player wins
    print("""              _                       
             (_)                      
    __      ___ _ __  _ __   ___ _ __ 
    \ \ /\ / / | '_ \| '_ \ / _ \ '__|
     \ V  V /| | | | | | | |  __/ |   
      \_/\_/ |_|_| |_|_| |_|\___|_|   """)


def hangman(secret_word):
    """The func. checks if the letter that guessed until now, if the letters match the secret word player wins
    :param secret_word: the secret word in the file
    :type secret_word: char
    :return: prints winner or losser
    """
    HANGMAN_ASCII_ART = """      _    _ 
     | |  | |
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |
                         |___/                           """
    MAX_TRIES = 6
    print(HANGMAN_ASCII_ART, "\n", MAX_TRIES, "\n" * 4)
    time.sleep(2)  # Makes the thread to sleep
    file_path = input("Enter file path (the text needs to be string of words separated by spaces:\n")
    while not (path.isfile(file_path)):  # checks for the correction of the path (if the path is valid)
        print("The path is wrong or not exsited, please enter new one:")
        file_path = input()
    index = input("Enter the index in which the secret word is in:\n")

    file_reader(file_path, index)  # Go to file_reader func. and performs the reading of the file
    secret_word = choose_word(file_path, index)  # By choose_word func. gives us the secret word
    print("\nLet's start!\n")
    num_of_tries = 1
    old_letters_guessed = []
    print(HANGMAN_PHOTOS[num_of_tries])
    print(show_hidden_word(secret_word, old_letters_guessed))

    while not (
            num_of_tries == MAX_TRIES + 1):  # While the number of tries is less then 6 keep getting a letter to guess
        letter = input("Guess a letter: ")
        if try_update_letter_guessed(letter, old_letters_guessed) == True and not (letter in secret_word):
            num_of_tries += 1  # Add 1 to number of tries
            print(":( \n\n")
            print(HANGMAN_PHOTOS[num_of_tries])  # Print the hangman position by number of tries
        show_hidden_word(secret_word, old_letters_guessed)
        print("\n")
        if check_win(secret_word, old_letters_guessed):  # If check_win returns true, print winner
            time.sleep(0.5)
            clear()
            winner()
            break
        if num_of_tries == MAX_TRIES + 1:  # If the player tried 6 times worng letters print loser
            time.sleep(0.5)
            clear()
            loser()
            break


def main():
    secret_word = ""
    hangman(secret_word)
    print("\n\n")
    input("Press any key to exit...")  # Help us maintain the screen of the game on


if __name__ == "__main__":
    main()
