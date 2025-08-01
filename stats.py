def get_num_of_words(text):
    words_list = text.split()
    return len(words_list)

def get_num_of_letters(text):
    counters = {}
    for l in text.lower():
        if l not in counters:
            counters[l] = 1
        else:
            counters[l] += 1
    return counters

def sort_on_character(item):
    return item["char"]

def sort_dictionary(dictionary):
    dictionary_list = []
    for key in dictionary:
        dictionary_list.append({"char": key, "num": dictionary[key]})
    dictionary_list.sort(key=sort_on_character)
    return dictionary_list