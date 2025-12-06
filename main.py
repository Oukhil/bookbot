import sys
from stats import get_num_words, get_num_characters, dictionary_sort

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")

    words = get_num_words(sys.argv[1])
    print(f"Found {words} total words")

    print("--------- Character Count -------")

    chars = get_num_characters(sys.argv[1])
    sorted_chars = dictionary_sort(chars)

    for i in sorted_chars:
        if i["char"].isalpha():
           print(f"{i["char"]}: {i["num"]}")


main()