def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def get_num_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    words = file_contents.split()

    return len(words)

def get_num_characters(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        file_contents_but_lower = file_contents.lower()
    
    char_dict = {}
    for i in file_contents_but_lower:
        if i in char_dict:
            char_dict[i] = char_dict[i] + 1
        else:
            char_dict[i] = 1
    
    return char_dict

def sort_on(items):
    return items["num"]

def dictionary_sort(dictionary):
    dictionary_list = []

    for i in dictionary:
        dictionary_list.append({"char":i, "num":dictionary[i]})

    dictionary_list.sort(reverse=True, key=sort_on)

    return dictionary_list
