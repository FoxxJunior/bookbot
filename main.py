# Set variables
path = "books/frankenstein.txt"
from stats import count

# Split the text in separate strings and return count
def main():
    num = count(path)
    print(num)

main()