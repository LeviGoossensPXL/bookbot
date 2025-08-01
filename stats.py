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