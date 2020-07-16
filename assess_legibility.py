from nlp import nlp
from get_knowledge import get_knowledge
from get_learned_lemmata import get_learned_lemmata
import json
import pickle

class Text:
    """
    This class should let us assess the legibility of a text

    ...
    
    Attributes
    ----------
    knowledge : a tuple of lists
        index 0 is a list of ITTB tags representing patterns students should know;
        index 1 is a list of vocab learned so far; this is hard coded for students
        who have just finished Latin 1

    learned_lemmata : list
        A list of lemmata produced by passing vocab through stanza

    text : list of strings
        each item in the list is a paragraph

    Methods
    -------
    process_paragraphs(text)
        process text paragraph by paragraph, then analyze sentences
    
    analyze_sentence(sentence):
        returns the sentence if >= 90% of the words are known

    word_form_known(word):
        returns 'True' if specific word form is in lexicon

    lemma_known(lemma):
        returns 'True' if lemma is known

    pattern_known(tag):
        returns 'True' if that pattern has been learned

    """
    def __init__(self,text):
        self.knowledge = get_knowledge()
        self.learned_lemmata = get_learned_lemmata()
        self.text = text

    def word_form_known(self,word):
        if word in self.knowledge[1]:
            return True

    def lemma_known(self,lemma):
        if lemma in self.learned_lemmata:
            return True

    def pattern_known(self,tag):
        if 'vgr' in tag:
            tag = tag[:-5]

        if tag in self.knowledge[0]:
            return True

    def process_text(self):
        """ concatenates list and evaluates sentences """
        continuous_text = ' '.join(text)
        doc = nlp(continuous_text)
        sentences = list(doc.sents)
        for sentence in sentences:
            self.analyze_sentence(sentence)

    def process_paragraphs(self):
        """ runs each paragraph through spacy, then evaluates sentences """
        reasonable_sentences = []
        text = self.text
        for paragraph in text:
#            doc = nlp(paragraph)
            sentences = list(text.sents)
            for sentence in sentences:
                if self.analyze_sentence(sentence):
                    reasonable_sentences.append(sentence)

        for rs in reasonable_sentences:
            print(rs)

    def assess_paragraph_difficulty(self):
        """ see how many words and how many unique words there are """
        assessment = []
        for paragraph in text:
            doc = nlp(paragraph)
            total_words = 0
            unique_words = []
            unique_lemmata = []
            for token in doc:
                if not token.is_punct:
                    total_words += 1
                    if token.text not in unique_words:
                        unique_words.append(token.text)
                    if token.lemma_ not in unique_lemmata:
                        unique_lemmata.append(token.lemma_)

            assessment.append(f"Total: {total_words}; Unique: {len(unique_words)}; Lemmata: {len(unique_lemmata)}")
            
        for a in assessment:
            print(a)

    def analyze_sentence(self,sentence):
        """ returns a sentence if more than 90% of words are known """
        
        sentence_length = len(sentence)
        
        known_words = 0

        for token in sentence:
            if self.word_form_known(token.text):
                known_words += 1
            elif self.lemma_known(token.lemma_) and self.pattern_known(token.tag_):
                known_words += 1

        if known_words / sentence_length >= 0.65:
            return True

if __name__ == '__main__':
    filename = 'smooshed-1.pickle'
#    filename = 'clean_inscriptions.json'
#    with open(filename,'r') as f:
#        text = json.load(f)
    with open(filename,'br') as f:
        text = pickle.load(f)

    work = Text(text)
    work.process_paragraphs()
