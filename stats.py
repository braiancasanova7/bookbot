def get_num_words(book):
    words = book.split()
    return len(words)


def get_char_num(book):
    char_num = {}
    for c in book:
        lowered = c.lower()
        if lowered in char_num:
            char_num[lowered] += 1
        else:
            char_num[lowered] = 1
    return char_num


def sort_on(items):
    return items["num"]


def sorted_list_dicts(char_count):
    count_list = []
    for char in char_count:
        dict_char = {"char": char, "num": char_count[char]}
        count_list.append(dict_char)
    count_list.sort(reverse=True, key=sort_on)
    return count_list
