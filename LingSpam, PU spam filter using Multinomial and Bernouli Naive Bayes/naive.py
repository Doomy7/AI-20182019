import common
import multinomialNB as mNB
import bernoulliNB as bNB
import scikitNB as sNB

split = 0.4
datasets = ['lingspam_public', 'pu_corpora_public']
datasetdir = {0 : ['bare', 'lemm', 'lemm_stop', 'stop'],
              1 : ['pu1', 'pu2', 'pu3', 'pua']}

def multinomialNB(words, SpamWord, LegitWord, X_train, y_train, X_test, y_test):
    SpamWord, LegitWord, prior = mNB.train(words, SpamWord, LegitWord, X_train, y_train)
    print("3130230 Multinomial Naive Bayes ")
    y_pred = mNB.predict(prior, SpamWord, LegitWord, X_test)
    print(common.A_P_R_F1(y_test, y_pred))
    print()

def bernoulliNB(words, X_train, y_train, X_test, y_test):
    SpamWord, LegitWord, prior = bNB.train(words, X_train, y_train)
    print("3130230 Bernoulli Naive Bayes")
    y_pred = bNB.predict(words, prior, SpamWord, LegitWord, X_test)
    print(common.A_P_R_F1(y_test, y_pred))

def scikitMNB(words, SpamWord, LegitWord, X_train, y_train, X_test, y_test):
    new_X_train, new_X_test = common.new_train_test(words, SpamWord, LegitWord, X_train, X_test)
    print("Scikit Multinomial Naive Bayes")
    y_pred = sNB.runMNB(new_X_train, y_train, new_X_test)
    print(common.A_P_R_F1(y_test, y_pred))

def scikitBNB(words, SpamWord, LegitWord, X_train, y_train, X_test,  y_test):
    new_X_train, new_X_test = common.new_train_test(words, SpamWord, LegitWord, X_train, X_test)
    print("Scikit Bernoulli Naive Bayes")
    y_pred = sNB.runBNB(new_X_train, y_train, new_X_test)
    print(common.A_P_R_F1(y_test, y_pred))

for dataset in range(len(datasets)):
    for subdir in range(len(datasetdir.get(dataset))):
        print("\nDataset : -> datasets\\" + datasets[dataset] + "\\" + datasetdir.get(dataset)[subdir])
        words, SpamWord, LegitWord, X_train, y_train, X_test, y_test = common.getWords_split(datasets[dataset], datasetdir.get(dataset)[subdir], split)
        multinomialNB(words, SpamWord, LegitWord, X_train, y_train, X_test, y_test)
        bernoulliNB(words, X_train, y_train, X_test, y_test)
        scikitMNB(words, SpamWord, LegitWord, X_train, y_train, X_test, y_test)
        scikitBNB(words, SpamWord, LegitWord, X_train, y_train, X_test, y_test)