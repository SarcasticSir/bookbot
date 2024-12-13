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
    
    path = ("testkontor/javielsker.txt")
    
    try:    
        text = open_book(path)
    except (FileNotFoundError, OSError):
        print("File not found. Please check the file path and try again. Exiting...")
        return


    word_count = count_words(text)
    title = get_title(path)
    

    print(f"--- Beginning analysis of {title} ---")
    print(    )
    print(f'Counting the words in "{title}"')
    print()
    print(f"The number of words found in {title} is: {word_count}.")


    lowercase_text = text.lower()
    lowerdict = {}
    for n in lowercase_text:
        lowerdict[n] = lowerdict.get(n, 0) + 1

    sorted_characters = sorted(lowerdict.items(), key=lambda item: item[1], reverse=True)
    print("Below is the frequency each character was used:")
    print()
    for char, count in sorted_characters:
        print(f"'{char}'was found: {count} time(s)")
    
    print()

    print("Success")
    print()
    print("--- End report ---")


main()