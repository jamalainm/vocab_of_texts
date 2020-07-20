import spacy

def lemma_and_form(doc):
    """ processes a spacy nlp doc and returns a dictionary of lemmata and word forms with freq """

    lemma_dict = {}

    for word in doc:
        # Eliminate punctuation
        if word.is_punct != True:
            # Up the lemma counter if the word's been registered already
            if word.lemma_ in lemma_dict:
                lemma_dict[word.lemma_]['freq'] += 1
                # Up the form counter if the form has been registered already
                if word.text in lemma_dict[word.lemma_]:
                    lemma_dict[word.lemma_][word.text] += 1
                # Add the word form and value 1 to the lemma
                else:
                    lemma_dict[word.lemma_].update({word.text : 1})
            # Add a lemma entry and the word form
            else:
                lemma_dict[word.lemma_] = {'freq' : 1, word.text : 1}

    # Sort the values so that the most frequent forms are listed first
    word_list = []

    for k,v in lemma_dict.items():
        new_e = {}
        new_v = sorted(v.items(), key=lambda x: x[1], reverse=True)
#        for i in new_v:
#            new_e[i[0]] = i[1]
        word_list.append({k : new_v})

    # Sort the dictionary so that most frequent lemmata are fronted
#    sorted_lemma_dict = sorted(lemma_dict.items(), key=lambda x: x[1]['freq'], reverse=True)
    sorted_lemma_dict = sorted(word_list,key=lambda x: list(x.values())[0][0][1], reverse=True)

#    return word_list
    return sorted_lemma_dict
