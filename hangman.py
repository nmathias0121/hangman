import random
import time

# let user input theme for game
def select_theme(words : dict) -> str:
    # get themes from dict
    themes = words.keys()

    # print options
    print('Select a theme :')
    i = 1
    for theme in themes :
        print(i, '.', theme)
        i += 1

    choice = int(input('Enter a number to proceed : '))

    # return chosen theme (i started from 1)
    return list(themes)[choice - 1]

# choose random word from given theme
def random_word(words : dict, theme : str) -> str :
    # shuffle list
    random.shuffle(list(words[theme]))

    # return random word
    return random.choice(list(words[theme]))

# get all indices of string that match the character
def indices_of(word : str, ch : str) -> list:
    lst_of_indices = []
    i = 0
    for letter in word:
        if letter == ch :
            lst_of_indices.append(i)
        i+=1
    
    return lst_of_indices

# game logic
def play_game(words : dict, theme : str) :
    game_word = random_word(words, theme)
    word_to_solve = '_' * len(game_word)

    # write function - print rules

    print("LET THE GAME BEGIN...")
    time.sleep(1)

    total_num_guesses = len(game_word) * 2
    for guess_num in range(total_num_guesses) :

        if word_to_solve == game_word:
            print('You are a winner!!')
            return
        
        print(word_to_solve)
        guess = input("Guess a character : ")

        if guess in game_word:
            # get occurences of guess in string
            indices = indices_of(game_word, guess)

            # replace character in word to solve
            # strings are immutable
            # convert to list, modify char at index & convert back to string
            lst = list(word_to_solve)
            for index in indices :
                lst[index] = guess
            word_to_solve = "".join(lst)
            
    print('You could have won :(')
    print('The word was ', game_word)