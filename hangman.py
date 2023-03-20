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

    choice = int(input())

    # return chosen theme (i started from 1)
    return list(themes)[choice - 1]

def random_word(dict, theme) :
    # shuffle list & return random word
    return random.choice(random.shuffle(dict[theme]))