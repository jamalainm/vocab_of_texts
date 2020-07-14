from nlp import nlp
from get_knowledge import get_knowledge

def get_learned_lemmata():
    """ Return a list of known lemmata """

    knowledge = get_knowledge()

    vocab = ' '.join(knowledge[1])

    nlp_vocab = nlp(vocab)

    lemmata = [token.lemma_ for token in nlp_vocab]

    return lemmata

if __name__ == '__main__':
    print(get_learned_lemmata())
