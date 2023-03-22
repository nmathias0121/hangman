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

    # user selects a theme
    theme = hangman.select_theme(words)

    hangman.play_game(words, theme)



if __name__ == "__main__":
    main()