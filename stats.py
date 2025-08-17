def get_book_words(filepath):
    filetext = ""
    words_list = []
    word_count = 0
    with open(filepath) as file:
        filetext = file.read()
    words_list = filetext.split()
    word_count = len(words_list)
    return word_count

def count_letters(filepath):
    filetext = ""
    letters = {}
    with open(filepath) as file:
        filetext = file.read()
    filetext = filetext.lower()
    for letter in filetext:
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] = letters[letter] + 1
    return letters