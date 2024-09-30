

from util import count_words, count_characters
def main():
    paragraph = input("Enter a paragraph: ").strip()
    word = count_words(paragraph)
    letter = count_characters(paragraph)
    print(f"Total words: {word}")
    print(f"Total letters: {letter}")

if __name__ == "__main__":
    main()
