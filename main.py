from stats import get_book_words, count_letters, sort_to_tide

def main():
    # print("input")
    # userpath = input() for later
    userpath = "books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found " + str(get_book_words(userpath)) + " total words")
    print("--------- Character Count -------")
    
    sorted = sort_to_tide(count_letters(userpath))
    for dict in sorted:
        if dict["char"].isalpha():
            print(dict["char"] + ": " + str(dict["num"]))

    print("============= END ===============")

main()