import spacy
from collections import Counter

def lemma_freq(doc):
    """ This function takes a spacy doc object and returns a list of tuples: word and freq. """

    # Don't count punctuation

    words = [token.lemma_ for token in doc if token.is_punct != True]

    word_freq = Counter(words)

    return word_freq.most_common()
