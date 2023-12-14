from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import joblib

class LemmaTokenizer:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
    def __call__(self, text):
        return [self.lemmatizer.lemmatize(word) for word in word_tokenize(text)]

# Step 1: Load the model and the vectorizer
model_filename = "sentiment_model.joblib"
vectorizer_filename = "tfidf_vectorizer.joblib"

logreg = joblib.load(model_filename)
tfidf_vectorizer = joblib.load(vectorizer_filename)

# Random text for prediction
random_text = '''One of the funniest movies in the last few decades. MUST SEE!'''


# Preprocess the text (if required) and perform TF-IDF vectorization using the original vectorizer
random_text_tfidf = tfidf_vectorizer.transform([random_text])

# Sentiment Prediction
sentiment_label = logreg.predict(random_text_tfidf)[0]

# Mapping the predicted label to sentiment
sentiment_map = {'0': "Negative", '1': "Positive"}
predicted_sentiment = sentiment_map[sentiment_label]

print(f"Predicted Sentiment: {predicted_sentiment}")


# --------------------------------------------------------------------------------


import pickle
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize

class LemmaTokenizer:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()

    def __call__(self, text):
        return [self.lemmatizer.lemmatize(word) for word in word_tokenize(text)]

# Step 1: Load the model and vectorizer using pickle
model_filename = "Model/sentiment_model.pkl"
vectorizer_filename = "Model/tfidf_vectorizer.pkl"

with open(model_filename, 'rb') as file:
    logreg = pickle.load(file)

with open(vectorizer_filename, 'rb') as file:
    tfidf_vectorizer = pickle.load(file)

# Random text for prediction
random_text = "This movie is absolutely fantastic! I highly recommend it."

# Preprocess the text (if required) and perform TF-IDF vectorization using the original vectorizer
random_text_tfidf = tfidf_vectorizer.transform([random_text])

# Sentiment Prediction
sentiment_label = logreg.predict(random_text_tfidf)[0]

# Mapping the predicted label to sentiment
sentiment_map = {'0': "Negative", '1': "Positive"}
predicted_sentiment = sentiment_map[sentiment_label]

print(f"Predicted Sentiment: {predicted_sentiment}")


# from LoadDataSet.DataSetLoader import return_dataframe_object
# from DataPreprocessing.StopWordsPerData import data_cleaning
# from sklearn.model_selection import train_test_split
# import numpy as np
# from nltk.stem import WordNetLemmatizer
# from nltk.tokenize import word_tokenize
# from sklearn.model_selection import train_test_split
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.model_selection import train_test_split
# from ModelSelection.Logistic_Regression import Logistic_Obj
# from Model_Losses.Losses import Evaluation_Parameters

# # Load The DataFrame
# df = return_dataframe_object()

# # Data Cleaning 
# df['Reviews_clean']=df['Reviews'].apply(data_cleaning)

# # Create the SubData frame
# data = df[['Reviews_clean', 'Reviews', 'Ratings', 'Label']]

# # devide into Train, Test Part
# train, test = train_test_split(data,test_size=.3,random_state=42, shuffle=True)

# # selected feature from train and test part
# train = train[['Reviews_clean', 'Label']]
# test = test[['Reviews_clean', 'Label']]

# class LemmaTokenizer:
#     def __init__(self):
#         self.lemmatizer = WordNetLemmatizer()
#     def __call__(self, text):
#         return [self.lemmatizer.lemmatize(word) for word in word_tokenize(text)]

# tfidf_vectorizer = TfidfVectorizer(max_features=10000, tokenizer=LemmaTokenizer())  

# # X_train Obj
# X_train_tfidf = tfidf_vectorizer.fit_transform(train['Reviews_clean'])

# # X_test_obj
# X_test_tfidf = tfidf_vectorizer.transform(test['Reviews_clean'])

# # y label same for all the data type
# y_train = train['Label']
# y_test = test['Label']


# model = Logistic_Obj(X_train_tfidf, y_train)

# y_pred = model.predict(X_test_tfidf)

# Evaluation_Parameters(y_test, y_pred)

# # import joblib
# # # Step 4: Save the model and vectorizer to files
# # model_filename = "Model/sentiment_model_try_1.joblib"
# # vectorizer_filename = "Model/tfidf_vectorizer_try_2.joblib"

# # # Save the model
# # joblib.dump(model, model_filename)

# # # Save the vectorizer
# # joblib.dump(tfidf_vectorizer, vectorizer_filename)