import math

def train(words, SpamWord, LegitWord, X_train, y_train):
    wordsSpam = dict.fromkeys(words.keys(), 0)
    wordsLegit = dict.fromkeys(words.keys(), 0)
    for key in SpamWord.keys():
        wordsSpam[key] = SpamWord[key]
    for key in LegitWord.keys():
        wordsLegit[key] = LegitWord[key]
    prior = []
    prior.append(y_train.count(0)/len(y_train))
    prior.append(y_train.count(1)/len(y_train))
    sumWordsSpam = dict.fromkeys(wordsSpam.keys(), 0)
    sumWordsLegit = dict.fromkeys(wordsLegit.keys(), 0)
    wholeSumSpam = 0
    wholeSumLegit = 0

    #count total number of words in each
    for key in words.keys():
        wholeSumSpam += wordsSpam[key]
        wholeSumLegit += wordsLegit[key]

    #count total number of occurances of word in each
    for file, label in zip(X_train, y_train):
        if label == 1:
            for key in file.keys():
                sumWordsSpam[key] += file[key]
        else:
            for key in file.keys():
                sumWordsLegit[key] += file[key]

    #get propabilities
    for key in words.keys():
        wordsSpam[key] = (sumWordsSpam[key]+1)/(wholeSumSpam+len(words))
        wordsLegit[key] = (sumWordsLegit[key]+1)/(wholeSumLegit+len(words))
    return wordsSpam, wordsLegit, prior


def predict(prior, SpamWord, LegitWord, X_test):
    y_pred = []
    for file in X_test:
        #init Scores
        scoreLegit = math.log(prior[0])
        scoreSpam = math.log(prior[1])
        for key in file.keys():
            scoreLegit += math.log(LegitWord[key])
            scoreSpam += math.log(SpamWord[key])
        if scoreLegit > scoreSpam:
            y_pred.append(0)
        else:
            y_pred.append(1)
    return y_pred