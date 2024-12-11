# Function to open text file
def open_book(path): # path to text file
    with open(path) as f: 
        return f.read() 
    
    
def count_words(text):
    words = text.split()
    return len(words)

def main():
    path = "books/Frankenstein.txt"
    text = open_book(path)
    word_count = count_words(text)
    print()
    print(f"The number of words are {word_count}")
main()