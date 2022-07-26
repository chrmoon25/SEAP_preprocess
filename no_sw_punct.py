# multiple language stopwords??

import os
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

all_tokens = list()

def read_html(w):
    with open(w, "r", encoding = "utf-8") as f:
        all_html = f.read()

    soup = BeautifulSoup(all_html, "html.parser")
    for data in soup(["style", "script"]):
        data.decompose()
    clean_html = " ".join(soup.stripped_strings)

    raw_tokens = word_tokenize(clean_html)

    stop_words = set(stopwords.words('english'))

    tokens = [w for w in raw_tokens if w.lower() not in stop_words]
    clean_tokens = list()
    
    for t in tokens:
        if t not in stop_words:
            clean_tokens.append(t)

    global cleaner_tokens
    cleaner_tokens = list()

    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    for t in clean_tokens:
        if t not in punc:
            cleaner_tokens.append(t)

    for t in cleaner_tokens:
        if t not in all_tokens:
            all_tokens.append(t)

def no_zero(t):    
    vector = {}
    for t in all_tokens:
        vector[t] = cleaner_tokens.count(t)
        if vector[t] == 0:
            vector.pop(t)
    print("FREQUENCY:", vector)


directory = "C:\\seap_test"
for filename in os.listdir(directory):
    indv_f = os.path.join(directory, filename)
    if os.path.isfile(indv_f):
        print("FILENAME:", filename)
        read_html(indv_f)
        no_zero(indv_f)
        print("\n")

        

if __name__ == "__main__":
    print("ALL TOKENS:")
    print(all_tokens)
