def get_num_words(book):
    words_list = []
    num_words = 0
    words_list = book.split()
    for word in words_list:
        num_words += 1
    return num_words


def get_num_chars_each(letters):
    chars_dict = dict()
    for letter in letters.lower():
        if letter in chars_dict:
            chars_dict[letter] += 1
        else:
            chars_dict[letter] = 1
    return chars_dict


def sort_on(items):
    return items["num"]


def get_sorted_list(chars):
    unsorted_list = []
    for char_key, char_count in chars.items():
        new_entry = {"char": char_key, "num": char_count}
        unsorted_list.append(new_entry)
    unsorted_list.sort(reverse=True, key=sort_on)
    return unsorted_list
