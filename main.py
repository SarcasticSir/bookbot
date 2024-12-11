import os


# Function to open text file
def open_book(path): # path to text file
    with open(path) as f: 
        return f.read()
    
# Removes file extension, returning just the title    
def get_title(path):
    filename = os.path.basename(path)
    title, _ = os.path.splitext(filename)
    return title
    
    
def count_words(text):
    words = text.split()
    return len(words)

def main():
    path = "books/Frankenstein.txt"
    text = open_book(path)
    word_count = count_words(text)
    title = get_title(path)

    print(f"Counting the words in {title}")
    input("Press Enter to show results")
    print()
    print(f"The number of words are {word_count}")
main()