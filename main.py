import sys
from stats import get_word_count, get_character_count, sort_characters

def get_book_text(file_path):
    with open(file_path) as book_file:
        file_contents = book_file.read()
        return file_contents

def print_report(path, num_words, character_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for line_item in character_count:
        if line_item["char"].isalpha():
            print(f"{line_item["char"]}: {line_item["num"]}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_word_count(text)
    character_count = sort_characters(get_character_count(text))
    print_report(path, num_words, character_count)


main()