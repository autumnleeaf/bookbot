import string

def get_text_length(text):
    text_dict = text.split()
    return len(text_dict)

def get_char_count(text):
    char_dict = {letter: 0 for letter in string.ascii_lowercase}
    for char in text:
        char = char.lower()
        if char in char_dict.keys():
            char_dict[char] += 1
    return char_dict

def get_sorted_dict(dict):
    list = []
    for key, value in dict.items():
        list.append({"char": key, "num": value})
    list.sort(key=lambda d: d['num'], reverse=True)
    return list