from stats import count_words, count_of_characters, sorted_list_dict
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(count_words(sys.argv[1]))
    print("--------- Character Count -------")
    book = sorted_list_dict(count_of_characters(sys.argv[1]))
    for char in book:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")


def get_book_test(book):
    with open(book) as b:
        content = b.read()
    return content
main()
