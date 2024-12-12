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
    
# Separates text by whitespace and counts the total    
def count_words(text):
    words = text.split()
    return len(words)

# Makes text lowercase
def make_lowercase(text):
    lowercase_text = text.lower()
    return lowercase_text


def main():
    
    path = input("Please enter the path to the text file: ")
    
    try:    
        text = open_book(path)
    except (FileNotFoundError, OSError):
        print("File not found. Please check the file path and try again. Exiting...")
        return
    

    word_count = count_words(text)
    title = get_title(path)

    print(f"Counting the words in '{title}'")
    input("Press Enter to show results")
    print()
    print(f"The number of words are {word_count}")
    print("Success")


main()