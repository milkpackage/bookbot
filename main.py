import sys

from stats import character_count, find_num_of_words, sorting_data



def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else: 
        path = sys.argv[1]
    text = get_book_text(path)
    num_of_words = find_num_of_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}... ")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    # print(character_count(text))
    sorting_data(text)
    for d in sorting_data(text):
        print(f"{d['char']}: {d['num']}")
    print("============= END ===============")


main()
