import random

def select_theme(dict) :
    # get themes from dict
    themes = dict.keys()

    # print options
    print('Select a theme :')
    i = 1
    for theme in themes :
        print(i, '.', theme)
        i += 1

    choice = int(input('Enter the number to select the theme : '))

    # return chosen theme (i started from 1)
    return list(themes)[choice - 1]

def random_word(dict, theme) :
    # shuffle list
    random.shuffle(list(dict[theme]))

    # return random word
    return random.choice(list(dict[theme]))

def play_game(dict, theme) :
    choose_word = random_word(dict, theme)
    print(choose_word)