from stats import count_book_words, count_book_characters, sort_dict_book_characters
import sys

def get_book_text(filepath):
    file_content = ""
    with open(filepath) as f:
        file_content = f.read()

    return file_content

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    content = get_book_text(book_path)
    num_words = count_book_words(content)

    print(f"""
        ============ BOOKBOT ============
        Analyzing book found at {book_path}...
        ----------- Word Count ----------
        Found {num_words} total words
        --------- Character Count -------
    """)
    characters_count = count_book_characters(content)
    ordered_dict = sort_dict_book_characters(characters_count)
    for dict in ordered_dict:
        print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")

main()
