from stats import get_num_of_words, get_num_of_letters, sort_dictionary
import sys
import platform

def get_book_text(filepath):
    with open(filepath, encoding="utf8") as f:
        return f.read()

def print_book_report(book_path):
    print("============ BOOKBOT ============")
    book_text = get_book_text(book_path)
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    num_words = get_num_of_words(book_text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    character_counters = get_num_of_letters(book_text)
    for character in sort_dictionary(character_counters):
        if character["char"].isalpha():
            print(f"{character["char"]}: {character["num"]}")
    print("============= END ===============")


def main():
    # book_path = "books/frankenstein.txt"
    # book_text = get_book_text(book_path)
    # print(book_text)
    # num_words = get_num_of_words(book_text)
    # print(f"{num_words} words found in the document")
    # letter_counters = get_num_of_letters(book_text)
    # print(letter_counters)
    # print(sort_dictionary(letter_counters))
    # print_book_report(book_path)

    if len(sys.argv) != 2:
        if platform.system() == "Linux":
            print("Usage: python3 main.py <path_to_book>")
        if platform.system() == "Windows":
            print("Usage: python main.py <path_to_book>")
        sys.exit(1)
    
    print_book_report(sys.argv[1])

main()