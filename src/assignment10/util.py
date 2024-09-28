from collections import Counter

def CountWord(word_list, word):
    word_counter = Counter(word_list)
    return word_counter[word]
