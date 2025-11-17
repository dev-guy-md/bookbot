from stats import count_words, count_chars, sorting_function
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
        num_words = contents.split()
    f.close()
    return contents

def arg_check(cmd_list):
    if len(cmd_list) == 2:
        return cmd_list[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def main():
#    fp = "boot.dev/bookbot/books/frankenstein.txt"
#    fp = sys.argv[1]
    fp = arg_check(sys.argv)
    book = get_book_text(fp)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {fp}...")
    print("----------- Word Count ----------")
    count_words(book)
    print("--------- Character Count -------")
    characters = count_chars(book)
    sorting_function(characters)
    print("============= END ===============")


main()
