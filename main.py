import web_scrape_words as scrape
import hangman


def main():
    # get words dict from web page with themes as keys & list of words as values
    words = scrape.get_words_create_files()

    '''
    files = words.keys()
    words_list = words.values()

    for file in list(files):
        print(file)
        '''

    repeat_game = True 

    while repeat_game == True :
        # user selects a theme
        theme = hangman.select_theme(words)

        hangman.play_game(words, theme)

        repeat = ''
        while (repeat.lower() not in ['y', 'n']) :
            repeat = input('\n Would you like to play another one? (Y/n) ')

        if repeat == 'y':
            repeat_game = True
        else :
            repeat_game = False
            print('**********Thank you for playing*********')
        



if __name__ == "__main__":
    main()