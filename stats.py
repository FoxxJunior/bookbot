# Set variable
path = "books/frankenstein.txt"

# Define dependant function
# Path is read out and content returned as string
def get_book_text(title):
    with open(title) as book:
        return book.read()

# Count the words
def count(path):
    content = get_book_text(path)
    words = content.split()
    return (f"Found {len(words)} total words")