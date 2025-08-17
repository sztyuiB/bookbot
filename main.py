from stats import get_book_words

def main():
    # print("input")
    # userpath = input() for later
    userpath = "books/frankenstein.txt"
    print(str(get_book_words(userpath)) + " words found in the document")

main()