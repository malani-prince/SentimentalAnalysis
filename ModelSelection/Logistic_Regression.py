from sklearn.linear_model import LogisticRegression

def Logistic_Obj(X_train_tfidf, y_train):
    logreg = LogisticRegression()
    model = logreg.fit(X_train_tfidf, y_train)
    return model
