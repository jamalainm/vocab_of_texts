import stanza
import spacy
from spacy_stanza import StanzaLanguage

def nlp(doc):
    """ Processes a text with spacy and stanza """

    snlp = stanza.Pipeline(lang="la")

    NLP = StanzaLanguage(snlp)

    return NLP(doc)
