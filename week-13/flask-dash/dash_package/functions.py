def sayhello():
    return "HELLO"

def twox(x):
    return x*2

def half(x):
    return x/2

def title():
    return "graph title!!!"


import pandas as pd
import pickle

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
english = set(nltk.corpus.words.words())



def preprocess(data):

    # lemmatize
    def lemmadata(doc):
        pattern = "([a-zA-Z]+(?:'[a-z]+)?)"
        raw_tokens = nltk.regexp_tokenize(doc, pattern)
        tokens = [i.lower() for i in raw_tokens]
        stop_words = set(stopwords.words('english'))
        listed = [w for w in tokens if not w in stop_words]
        lemmatized = [wordnet_lemmatizer.lemmatize(word, pos="v") for word in listed]
        lemmatized = list(filter(lambda w: w != 'lb', lemmatized))
        words = list(filter(lambda w: w in english, lemmatized))
        return " ".join(words)

    lemmatized = [lemmadata(post) for post in data]

    # picked tfidf vectorizer
    tfidf = pickle.load(open("dash_package/pickles/tfidf.pkl", "rb"))

    transformed = tfidf.transform(lemmatized)
    tfidf_df = pd.DataFrame(transformed.toarray(), columns=tfidf.get_feature_names())

    # pickled the list of relevant words
    relevant = pickle.load(open("dash_package/pickles/relevantwords.pkl", "rb"))

    testset = [tfidf_df[word] for word in relevant if word in tfidf_df.columns]

    return pd.DataFrame(testset).transpose()


def classify_text(text):
    # the model
    mnb = pickle.load(open("dash_package/pickles/mnb.pkl", "rb"))
    listtext = [text]
    processed = preprocess(listtext)
    result = mnb.predict(processed)[0]

# version 1
    # if result == 0:
    #     return 'Category: Art'
    #
    # if result == 1:
    #     return 'Category: Programming'
    #
    # else:
    #     return 'Classifier Down'


# version 2
    return result
