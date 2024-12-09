def main():
    with open("books/Frankenstein.txt") as f:
        # Åpner frankenstein tror jeg
        file_contents = f.read()
        print(file_contents)
main()