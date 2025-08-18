import sys
from stats import get_book_words, count_letters, sort_to_tide

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    userpath = sys.argv[1]
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + userpath + "...")
    print("----------- Word Count ----------")
    print("Found " + str(get_book_words(userpath)) + " total words")
    print("--------- Character Count -------")
    
    sorted = sort_to_tide(count_letters(userpath))
    for dict in sorted:
        if dict["char"].isalpha():
            print(dict["char"] + ": " + str(dict["num"]))

    print("============= END ===============")

main()