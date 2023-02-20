def letter_frequency(sentence):
    """
    Determine the number of times a letter occurs in a sentence.
    """
    frequencies = {}
    for letter in sentence:
        frequency = frequencies.setdefault(letter, 0)
        frequencies[letter] = frequency + 1
    return frequencies

from collections import defaultdict
def letter_frequencies(sentence):
    """
    Determine the number of times a letter occurs in a sentence while using
    the defaultdict module from collections library.
    """
    frequencies = defaultdict(int)
    for letter in sentence:
        frequencies[letter] += 1
    return frequencies

from collections import Counter
def letter_counter(sentence):
    """
    Determine the number of times a letter occurs in a sentence by using the
    Counter module from the collections library.
    """
    return Counter(sentence)
