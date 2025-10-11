def count_words(text):
    with open(text) as b:
        content = b.read()
    content = len(content.split())

    return f"Found {content} total words"

def count_of_characters(text):
    with open(text) as b:
        content = b.read()
    content.split()
    dict_count_character = {}
    for character in content:
        c = character.lower()
        if c not in dict_count_character:
            dict_count_character[c] = 1
        else:
            dict_count_character[c] += 1
    return dict_count_character

def sorted_list_dict(dict_characters):
    list_dict = []
    for char in dict_characters:
        new_dict = {}
        value = dict_characters[char]
        new_dict["char"] = char
        new_dict["num"] = value
        list_dict.append(new_dict)
    def sort_on(list_dict):
        return list_dict["num"]
    list_dict.sort(reverse=True, key=sort_on)
     
    return list_dict


