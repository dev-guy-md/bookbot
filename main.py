from stats import count_words, count_chars, sorting_function
#import stats

def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
        num_words = contents.split()
    f.close()
    return contents

def main():
    fp = "books/frankenstein.txt"
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
