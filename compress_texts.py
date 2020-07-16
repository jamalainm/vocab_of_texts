import json
from nlp import nlp
import pickle
from spacy.tokens import DocBin

def load_inscriptions():
    with open('dbg1.json','r') as f:
        return json.load(f)

def pickle_inscriptions(corpus):
    """ pickle the tens of thousands of inscriptions . . . . """

    doc = nlp(corpus)


    with open(f'smooshed-1.pickle','wb') as f:
        pickle.dump(doc, f)

#    pickle.dump(to_be_pickled, open('save.p','wb'))

def bin_inscriptions(corpus):
    """ put the texts into the docbin """
    doc_bin = DocBin(attrs=["LEMMA","TAG","POS","DEP","HEAD"], store_user_data=True)
    for c in corpus:
        doc = nlp(c)
        doc_bin.add(doc)

    with open('dbg.bin','wb') as f:
        f.write(doc_bin.to_bytes())

if __name__ == '__main__':
    with open('smooshed-1.txt','r') as f:
        corpus = f.read()
    pickle_inscriptions(corpus)
