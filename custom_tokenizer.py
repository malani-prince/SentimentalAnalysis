import nltk
# nltk.download('punkt')
# nltk.download('wordnet')

class LemmaTokenizer:
    def __init__(self):
        self.lemmatizer = nltk.WordNetLemmatizer()

    def __call__(self, text):
        return [self.lemmatizer.lemmatize(word) for word in nltk.word_tokenize(text)]
