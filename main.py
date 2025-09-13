from stats import count_words, count_characters, sorted_list_dictionary
from curses.ascii import isalpha
import sys

def main():
    #book = get_book_text("./books/frankenstein.txt")
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    num_words = count_words(sys.argv[1])
    count_char = count_characters(sys.argv[1])
    sorted_list = sorted_list_dictionary(count_char)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
def get_book_text(filepath):
    book_content = ""

    with open(filepath) as f:
        book_content = f.read()

    return book_content


main()
