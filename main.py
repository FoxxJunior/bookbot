# Set variables
path = "books/frankenstein.txt"
from stats import count, get_book_text, characters

# List each character including symbols and spaces and count
def main():
    text = get_book_text(path)
    result = characters(text)
    print(result)

main()