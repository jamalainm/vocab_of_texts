from lemma_and_form import lemma_and_form
import pickle

def print_common_words(word_list):
    counter = 0
    while counter < 900:
        print(f"{counter + 1} - {word_list[counter]}")
        counter += 1

if __name__ == '__main__':
    text = 'smooshed-1'
    with open(f'../Archive_Text/Barrel/{text}.pickle','rb') as f:
        doc = pickle.load(f)
    word_list = lemma_and_form(doc)
    print_common_words(word_list)
