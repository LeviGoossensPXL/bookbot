from stats import get_num_of_words, get_num_of_letters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    book_text = get_book_text("books/frankenstein.txt")
    # print(book_text)
    num_words = get_num_of_words(book_text)
    # print(f"{num_words} words found in the document")
    letter_counters = get_num_of_letters(book_text)
    print(letter_counters)

main()