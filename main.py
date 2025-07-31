def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_num_of_words(text):
    words_list = text.split()
    return len(words_list)

def main():
    book_text = get_book_text("books/frankenstein.txt")
    # print(book_text)
    num_words = get_num_of_words(book_text)
    print(f"{num_words} words found in the document")

main()