import nltk, re, pprint
from nltk import word_tokenize
from nltk import sent_tokenize
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

import time

from nltk.tokenize import word_tokenize

from nltk.parse.corenlp import CoreNLPParser
from nltk.tag import StanfordNERTagger
import csv
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn import tree
import graphviz
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from numpy import array
from sklearn.preprocessing import OneHotEncoder
from nltk.stem.snowball import SnowballStemmer


def dt_classification():
    global feature_cols
    t1 = time.time()
    dataset = pd.read_csv("DT2.csv", header=0)
    print(dataset.shape)
    X = dataset.values[:, 0:-1]
    Y = dataset.values[:, -1]
    # print(Y)
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
    classifier = DecisionTreeClassifier()
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    # print(y_pred)
    accuracy = accuracy_score(y_test, y_pred)*100
    matrix = confusion_matrix(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    print("Accuracy: ", accuracy)
    print("Confusion matrix: \n", matrix)
    print("Classification report: \n", report)
    t2 = time.time()
    print("Execution time: ", t2-t1)
    dot_data = tree.export_graphviz(classifier, out_file=None, filled=True, rounded=True, special_characters=True,
                                    feature_names=feature_cols, class_names=['0', '1', '2', '3'])
    graph = graphviz.Source(dot_data)
    graph.render("iris")

    dump(classifier, 'classifier2.joblib')


def classification_test():

    t1 = time.time()
    dataset = pd.read_csv("DT2.csv", header=None)
    print(dataset.shape)
    X = dataset.values[:, 0:-1]
    Y = dataset.values[:, -1]
    X_train, X_test, y_train, y_test = train_test_split (X, Y, test_size=0.3, random_state=42)

    classifier = load('classifier2.joblib')
    # classifier.predict()

    y_pred = classifier.predict(X_test)
    # print(y_pred)
    accuracy = accuracy_score(y_test, y_pred) * 100
    matrix = confusion_matrix(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    print("Accuracy: ", accuracy)
    print("Confusion matrix: \n", matrix)
    print("Classification report: \n", report)
    t2 = time.time()
    print("Execution time: ", t2 - t1)
    dot_data = tree.export_graphviz(classifier, out_file=None)
    graph = graphviz.Source(dot_data)
    graph.render("iris")