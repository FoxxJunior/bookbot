# Set variables
path = "books/frankenstein.txt"

# Split the text in separate strings and return count
def main():
    content = get_book_text(path)
    words = content.split()
    print(f"Found {len(words)} total words")

# Path is read out and content returned as string
def get_book_text(title):
    with open(title) as book:
        return book.read()

main()