import web_scrape_words as scrape


def main():
    words = scrape.get_words_create_files()

    files = words.keys()
    words_list = words.values()

    for file in list(files):
        print(file)

if __name__ == "__main__":
    main()