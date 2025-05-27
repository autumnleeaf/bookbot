from stats import get_text_length
from stats import get_char_count
from stats import get_sorted_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def pretty_print(sorted_chars):
    for item in sorted_chars:
        print("{}: {}".format(item['char'], item['num']))

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    filepath = sys.argv[1]
    print("Analyzing book found at", filepath)
    text = get_book_text(filepath)
    print("----------- Word Count ----------")
    text_length = get_text_length(text)
    print("Found",text_length ,"total words")
    print("--------- Character Count -------")
    sorted_chars = get_sorted_dict(get_char_count(text))
    pretty_print(sorted_chars)
    print("============= END ===============")

main()