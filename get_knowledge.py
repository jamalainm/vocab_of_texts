import mysql.connector
from unidecode import unidecode
import json

def get_knowledge():
    """ poll the db and return a tuple of lists: patterns, vocab """

    with open('info.json','r') as f:
        data = json.load(f)

    mydb = mysql.connector.connect(
            host=data['host'],
            port=data['port'],
    #        database="curriculum",
            user=data["user"],
            password=data["password"],
            auth_plugin='mysql_native_password'
            )
# Get ITTB codes for word forms known
    grammar = mydb.cursor()

    grammar.execute("SELECT ITTB_Code FROM curriculum.cll_grammar_topics WHERE unit = 1 or unit = 2 or unit = 3")
# Get the codes out of tuple and into list
    patterns = []

    for g in grammar:
        if len(g) > 0:
            patterns.append(g[0])

# Get the phrases learned so far
    vocab = mydb.cursor()

    vocab.execute("SELECT phrase FROM Verba.seventeen")
# Get the vocab out of tuple and into list
    phrases = [v[0] for v in vocab]
# Get rid of slashes, hyphenates; unidecode, and lowercase
    words = []

    for p in phrases:
        new_phrase = p.split(' ')
        for np in new_phrase:
            np = np.lower()
            np = unidecode(np)
            if np[0] != '-' and np not in words:
                words.append(np)

    return (patterns, words)


