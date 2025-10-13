# User input translated to path and function called
def main():
    path = "books/frankenstein.txt"
    content = get_book_text(path)
    print(content)

# Path is read out and content returned as string
def get_book_text(path):
    with open(path) as book:
        string = book.read()
    return string

main()