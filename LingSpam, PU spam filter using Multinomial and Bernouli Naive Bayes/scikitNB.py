from sklearn.naive_bayes import MultinomialNB, BernoulliNB


def runMNB(X_train, y_train, X_test):
    clf = MultinomialNB()
    new_X_train = []
    new_X_test = []
    #array transformation
    for dict in X_train:
        new_X_train.append(list(dict.values()))
    for dict in X_test:
        new_X_test.append(list(dict.values()))
    clf.fit(new_X_train, y_train)
    y_pred = clf.predict(new_X_test)
    return y_pred

def runBNB(X_train, y_train, X_test):
    clf = BernoulliNB()
    new_X_train = []
    new_X_test = []
    #array transformation
    for dict in X_train:
        new_X_train.append(list(dict.values()))
    for dict in X_test:
        new_X_test.append(list(dict.values()))
    clf.fit(new_X_train, y_train)
    y_pred = clf.predict(new_X_test)
    return y_pred