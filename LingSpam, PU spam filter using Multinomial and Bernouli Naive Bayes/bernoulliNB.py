import math

def train(words, X_train, y_train):
    prior = []
    prior.append(y_train.count(0)/len(y_train))
    prior.append(y_train.count(1)/len(y_train))
    wordsSpam = dict.fromkeys(words.keys(), 0)
    wordsLegit = dict.fromkeys(words.keys(), 0)
    for word in words:
        filesSpam = 0
        filesLegit = 0
        for file, label in zip(X_train, y_train):
            if label == 1:
                if word in file:
                    filesSpam += 1
            else:
                if word in file:
                    filesLegit += 1
        wordsSpam[word] += (filesSpam+1)/(y_train.count(1)+2)
        wordsLegit[word] += (filesLegit+1)/(y_train.count(0)+2)
    return wordsSpam, wordsLegit, prior


def predict(words, prior, SpamWord, LegitWord, X_test):
    y_pred = []
    for file in X_test:
        #init Scores
        scoreLegit = math.log(prior[0])
        scoreSpam = math.log(prior[1])
        for word in words:
            if word in file:
                scoreLegit += math.log(LegitWord[word])
                scoreSpam += math.log(SpamWord[word])
            else:
                scoreLegit += math.log(1 - LegitWord[word])
                scoreSpam += math.log(1 - SpamWord[word])
        if scoreLegit > scoreSpam:
            y_pred.append(0)
        else:
            y_pred.append(1)
    return y_pred