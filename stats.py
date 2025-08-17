def get_book_words(filepath):
    filetext = ""
    words_list = []
    word_count = 0
    with open(filepath) as file:
        filetext = file.read()
    words_list = filetext.split()
    word_count = len(words_list)
    return word_count