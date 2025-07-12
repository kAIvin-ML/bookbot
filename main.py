import sys
from stats import get_num_words, get_num_chars_each, get_sorted_list

def main():
    if len(sys.argv) != 2:
        print("Try again.")
        print("The command should look like this:")
        print("Usage: python3 main.py <path_to_book>")
        print("For instance: python3 main.py books/frankenstein.txt")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    num_chars_each = get_num_chars_each(text)
    print(num_chars_each)
    sorted_list = get_sorted_list(num_chars_each)
    print_report(sorted_list, book_path, num_words)


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def print_report(list, book_path, num_words):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for l in list:
        if l["char"].isalpha():
            print(f"{l["char"]}: {l["num"]}")
    print("============= END ===============")


main()
