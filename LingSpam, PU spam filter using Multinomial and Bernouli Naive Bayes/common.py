import os
import random

def getWords_split(dataset, subfolder, split):
    # init basic
    words = {}
    SpamWord = {}
    LegitWord = {}
    X_train = []
    y_train = []
    X_test = []
    y_test = []
    # scan subfolders
    for root, dirs, files in os.walk("datasets\\" + dataset + "\\" + subfolder):
        for file in files:
            # random split
            train = random.randint(0, 10) / 10 > split
            # open file
            datafile = open(root + "\\" + file, "r")
            # init file words
            file_words = {}
            # from file name check if spam
            if "spmsg" in file:
                # label for spam
                label = 1
                # scan file
                for line in datafile:
                    for word in line.split():
                        # built file word dict
                        file_words[word] = 1 if word not in file_words else file_words[word] + 1
                        # if file is for used for train update vocabulary and labeledVoc
                        if train:
                            words[word] = 1 if word not in words else words[word] + 1
                            SpamWord[word] = 1 if word not in SpamWord else SpamWord[word] + 1
                        # patching word found in test but is not in train
                        else:
                            if word not in words:
                                words[word] = 0
            # same for legit file
            else:
                label = 0
                for line in datafile:
                    for word in line.split():
                        file_words[word] = 1 if word not in file_words else file_words[word] + 1
                        if train:
                            words[word] = 1 if word not in words else words[word] + 1
                            LegitWord[word] = 1 if word not in LegitWord else LegitWord[word] + 1
                        # patching word found in test but is not in train
                        else:
                            if word not in words:
                                words[word] = 0

            # update test and train set
            if train:
                X_train.append(file_words)
                y_train.append(label)
            else:
                X_test.append(file_words)
                y_test.append(label)
    return words, SpamWord, LegitWord, X_train, y_train, X_test, y_test


def A_P_R_F1(y_true, y_pred):
    TP = 0
    FP = 0
    TN = 0
    FN = 0
    for i in range(len(y_pred)):
        if y_pred[i] == 1:
            if y_pred[i] == y_true[i]:
                TP += 1
            else:
                FP += 1
        else:
            if y_pred[i] == y_true[i]:
                TN += 1
            else:
                FN += 1
    accuracy = (TP + TN) / (TP + TN + FP + FN)
    if TP + FP == 0:
        precision = 0
    else:
        precision = TP / (TP + FP)
    if TP + FN == 0:
        recall = 0
    else:
        recall = TP / (TP + FN)
    if recall + precision == 0:
        f1 = 0
    else:
        f1 = (2 * recall * precision) / (recall + precision)
    return "Evaluation block -> " \
           " accuracy: " + str(accuracy) + \
           " precision: " + str(precision) + \
           " recall: " + str(recall) + \
           " f1: " + str(f1)

def new_train_test(words, SpamWord, LegitWord, X_train, X_test):
    wordsSpam = dict.fromkeys(words.keys(), 0)
    wordsLegit = dict.fromkeys(words.keys(), 0)
    new_X_train = []
    new_X_test = []
    for key in SpamWord.keys():
        wordsSpam[key] = SpamWord[key]
    for key in LegitWord.keys():
        wordsLegit[key] = LegitWord[key]

    for file in X_train:
        tempDict = dict.fromkeys(words.keys(), 0)
        for key in file:
            tempDict[key] = file[key]
        new_X_train.append(tempDict)

    for file in X_test:
        tempDict = dict.fromkeys(words.keys(), 0)
        for key in file:
            tempDict[key] = file[key]
        new_X_test.append(tempDict)
    return new_X_train, new_X_test