
def count_words(paragraph):

    words = paragraph.split()
    return len(words)

def count_characters(paragraph):

    return sum(1 for char in paragraph if char.isalpha())
