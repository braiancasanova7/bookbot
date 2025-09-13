def count_words(filepath):
    book_content = ""
    words = None
    count_words = 0

    with open(filepath) as f:
        book_content = f.read()
        words = book_content.split()
    for word in words:
        count_words +=1

    return count_words

def count_characters(filepath):
    book_content = ""
    chars_dict = {}

    with open(filepath) as f:
        book_content = f.read()

    book_content = book_content.lower()

    for char in book_content:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1

    return chars_dict

def sorted_list_dictionary(dictionary):
    list_dictionarys = []
    for c in dictionary:
        dictionary_list = {}
        dictionary_list["char"] = c
        dictionary_list["num"] = dictionary[c]
        list_dictionarys.append(dictionary_list)

    def sort_on(items):
        return items["num"]

    list_dictionarys.sort(reverse=True, key=sort_on)
    return list_dictionarys
