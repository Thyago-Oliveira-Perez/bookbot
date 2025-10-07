def count_book_words(book_content):
    return len(book_content.split())

def count_book_characters(book_content):
    dic_characters = {}
    book_content = book_content.lower()
    for character in book_content:
        if character in dic_characters:
            dic_characters[character] += 1
        else:
            dic_characters[character] = 1

    return dic_characters

def sort_on(dict):
    return dict["num"]

def sort_dict_book_characters(dict_characters):
    dict_list = []
    for dict_character in dict_characters:
        dict_list.append({"char": dict_character, "num": dict_characters[dict_character]})
    
    dict_list.sort(reverse=True, key=sort_on)

    return dict_list