# Set variable
path = "books/frankenstein.txt"

# Define/import dependant functions
# Path is read out and content returned as string
def get_book_text(path):
    with open(path) as book:
        return book.read()

# Count the words
def count(path):
    content = get_book_text(path)
    words = content.split()
    return (f"Found {len(words)} total words")

# Define the number of characters
def characters(string):
    character_count = {}
    lowercase = string.lower()
    for each in lowercase:
        if each in character_count:
            character_count[each] += 1
        else: character_count[each] = 1
    return character_count