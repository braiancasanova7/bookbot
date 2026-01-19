import sys

from stats import get_char_num, get_num_words, sort_on, sorted_list_dicts


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count = get_char_num(text)
    sorted_count = sorted_list_dicts(character_count)
    print_report(book_path, num_words, character_count, sorted_count)


def get_book_text(book):
    with open(book) as book:
        return book.read()


def print_report(book_path, num_words, character_count, sorted_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_count:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()
