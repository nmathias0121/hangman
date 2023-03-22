import random
import time

def select_theme(dict) :
    # get themes from dict
    themes = dict.keys()

    # print options
    print('Select a theme :')
    i = 1
    for theme in themes :
        print(i, '.', theme)
        i += 1

    choice = int(input('Enter a number to proceed : '))

    # return chosen theme (i started from 1)
    return list(themes)[choice - 1]

def random_word(dict, theme) :
    # shuffle list
    random.shuffle(list(dict[theme]))

    # return random word
    return random.choice(list(dict[theme]))

def indices_of(str, ch) :
    lst_of_indices = []
    i = 0
    for letter in str:
        if letter == ch :
            lst_of_indices.append(i)
        i+=1
    
    return lst_of_indices

def play_game(dict, theme) :
    game_word = random_word(dict, theme)
    word_to_solve = '_' * len(game_word)

    # write function - print rules

    print("LET THE GAME BEGIN...")
    time.sleep(1)

    total_num_guesses = len(game_word) * 2
    for guess_num in range(total_num_guesses) :
        
        print(word_to_solve)
        guess = input("Guess a character : ")

        if guess in game_word:
            # get occurences of guess in string
            indices = indices_of(game_word, guess)
            # replace character in word to solve
            for index in indices :
                word_to_solve[index] = guess
            

    print(game_word)