from stats import get_book_words, count_letters

def main():
    # print("input")
    # userpath = input() for later
    userpath = "books/frankenstein.txt"
    print(str(get_book_words(userpath)) + " words found in the document")
    print(count_letters(userpath))

main()