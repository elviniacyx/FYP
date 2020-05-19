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


import pickle
from joblib import dump, load

ne_key = []
ne_value = ['LOCATION', 'PERSON', 'ORGANIZATION', 'MISC']
feature_cols = []
stem_dict = []


def extract_webpage_titles():

    urls = open('web_links.txt', "r")
    urls_nospace = open('web_links_clean.txt', "w+")
    contents = open('titles_raw.txt', "w+")
    # sentences = open('contents_raw.txt', "w+")

    for line in urls:
        if not line.isspace():
            urls_nospace.write(line)
    urls_nospace.seek(0)

    for x in urls_nospace:
        try:
            url = x
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            soup = BeautifulSoup(urlopen(req), 'html.parser')
            soup.prettify()
            title = soup.title.string
            # paragraphs = soup.find_all('p')
            # for p in paragraphs:
            #     text = p.getText()
            #     sentences.write(text + '\n')

            contents.write(title + '\n')
            # sentences.write('\n\n')
        except:
            print("Failed. Trying others.")
            continue

    urls.close()
    urls_nospace.close()
    contents.close()
    # sentences.close()


def extract_content_keywords():

    contents = open('contents_raw.txt', "r")
    contents_a = open('contents_inter.txt', "w+")
    contents_b = open('contents_final.txt', "w+")

    for content in contents:
        sents = sent_tokenize(content)
        for sent in sents:
            tokens = word_tokenize(sent)
            for token in tokens:
                if r"apple" in token.lower():
                    contents_a.write(sent + '\n')
                    break

    contents_a.close()
    contents_a = open("contents_inter.txt", "r")

    for a in contents_a:
        tokens = word_tokenize(a)
        for token in tokens:
            if r"buddy" in token.lower():
                contents_b.write(a + '\n')
                break

    contents.close()
    contents_a.close()
    contents_b.close()


def extract_title_keywords():

    t1 = time.time()

    titles = open('titles_raw.txt', "r")

    # global ne_key
    global ne_value
    global feature_cols
    global stem_dict

    # ne_key = []
    # ne_value = ['LOCATION', 'PERSON', 'ORGANIZATION', 'MISC']

    prettt = [[], []]

    st = StanfordNERTagger(
        '/Users/yixuancui/Downloads/stanford-ner-2018-10-16/classifiers/english.all.3class.distsim.crf.ser.gz',
                           '/Users/yixuancui/Downloads/stanford-ner-2018-10-16/stanford-ner.jar', encoding='utf-8')


    titles_c_list = []
    for title in titles:
        titles_c_list.append(title)
    print("Length of titles_a_list: ", len(titles_c_list))

    label_list = []
    counter = 0

    titles_d_list = []
    titles_ner1_list = []
    titles_ner2_list = []
    words_in_between = []
    v_list = []
    n_list = []
    r_list = []
    j_list = []
    d_list = []
    i_list = []
    stem_list = []

    for c in titles_c_list:
        text = c
        if not text:
            continue

        print(counter)
        # label = input(c)
        # label_list.append(int(label))
        label_list = [1] * 50 + [2] * 50 + [3] * 50 + [4] * 50 + [5] * 50 + [6] * 50

        v_count = 0
        n_count = 0
        r_count = 0
        j_count = 0
        d_count = 0
        i_count = 0
        stem_check = 0
        # todo 这里已经把index提取出来了，接下来可以把index1之前，1和2之间，2之后的所有名词和动词提取出来，加pos，stemmer怎么用再说吧我也不知道
        tokenized_text = word_tokenize(text)
        classified_text = st.tag(tokenized_text)
        pos_tagger = CoreNLPParser(url='http://localhost:9000', tagtype='pos')
        pos = list(pos_tagger.tag(tokenized_text))
        ss = SnowballStemmer("english")

        index = []
        for i in range(len(classified_text)):
            word = classified_text[i][0]
            tag = classified_text[i][1]
            if tag != 'O':
                # print('NE: ', word, ', Tag: ', tag, ', Index: ', i)
                # if word.lower() not in ne_key:
                #     ne_key.append(word.lower())
                index.append(i)
        pre_oh_classified_text_0 = [classified_text[i][0].lower() for i in index]
        pre_oh_classified_text_1 = [classified_text[i][1] for i in index]
        if not pre_oh_classified_text_0:
            pre_oh_classified_text_0 = ['None']
        if not pre_oh_classified_text_1:
            pre_oh_classified_text_1 = ['None']
        prettt[0].append(pre_oh_classified_text_0)
        prettt[1].append(pre_oh_classified_text_1)
        counter += 1

        # for i in range(len(classified_text)):
        #     if ss.stem(word) in ['acquir', 'buy', 'purchas', 'acquisit']:
        #         stem_check = 1
        #         break
        for i in range(len(classified_text)):
            if pos[i][1] in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']:
                v_count += 1
                word_stem = ss.stem(pos[i][0].lower())
                stem_list.append(word_stem)
                if word_stem not in stem_dict:
                    stem_dict.append(word_stem)
            if pos[i][1] in ['NN', 'NNS', 'NNP', 'NNPS']:
                n_count += 1
                # word_stem = ss.stem(pos[i][0].lower())
                # stem_list.append(word_stem)
                # if word_stem not in stem_dict:
                #     stem_dict.append(word_stem)
            if pos[i][1] in ['RB', 'RBR', 'RBS', 'RP']:
                r_count += 1
            if pos[i][1] in ['JJ', 'JJR', 'JJS']:
                j_count += 1
            if pos[i][1] in ['DT']:
                d_count += 1
            if pos[i][1] in ['IN']:
                i_count += 1
        v_list.append(v_count)
        n_list.append(n_count)
        r_list.append(r_count)
        j_list.append(j_count)
        d_list.append(d_count)
        i_list.append(i_count)
        # stem_list.append(stem_check)

    # enc1 = OneHotEncoder(handle_unknown='ignore')
    # enc1.fit(array(ne_key).reshape(-1, 1))
    enc2 = OneHotEncoder(handle_unknown='ignore')
    enc2.fit(array(ne_value).reshape(-1, 1))
    enc3 = OneHotEncoder(handle_unknown='ignore')
    enc3.fit(array(stem_dict).reshape(-1, 1))

    onehot_list = []

    for j in range(len(titles_c_list)):
        # onehot_ner1 = enc1.transform(array(prettt[0][j]).reshape(-1, 1)).toarray().tolist()
        # nekeys = [sum(i) for i in zip(*onehot_ner1)]
        onehot_ner2 = enc2.transform(array(prettt[1][j]).reshape(-1, 1)).toarray().tolist()
        nevalues = [sum(i) for i in zip(*onehot_ner2)]
        onehot_ner3 = enc3.transform(array(stem_list[j]).reshape(-1, 1)).toarray().tolist()
        stemlists = [sum(i) for i in zip(*onehot_ner3)]
        # join = nekeys + nevalues + stemlists
        join = nevalues + stemlists
        onehot_list.append(join)

    # header_list = ne_key + ne_value + ["v_list", "n_list", "r_list", "j_list", "d_list", "i_list", "stem_list", "label"]
    # feature_cols = ne_key + ne_value + ["v_list", "n_list", "r_list", "j_list", "d_list", "i_list", "stem_list"]
    header_list = ne_value + stem_dict + ["v_list", "n_list", "r_list", "j_list", "d_list", "i_list", "label"]
    feature_cols = ne_value + stem_dict + ["v_list", "n_list", "r_list", "j_list", "d_list", "i_list"]

    ll = [onehot_list[i] + [v_list[i]] + [n_list[i]] + [r_list[i]] + [j_list[i]]
          + [d_list[i]] + [i_list[i]] + [label_list[i]] for i in range(len(onehot_list))]
    # ll = [onehot_list[i] + [v_list[i]] + [n_list[i]] + [r_list[i]] + [j_list[i]]
    #       + [d_list[i]] + [i_list[i]] + [stem_list[i]] + [label_list[i]] for i in range(len(onehot_list))]
    # ll = [onehot_list[i] + [v_list[i]] + [n_list[i]] + [r_list[i]] + [j_list[i]]
    #       + [d_list[i]] + [i_list[i]] + [stem_list[i]] for i in range(len(onehot_list))]

    with open('DT2.csv', mode='w') as DT:
        dt_writer = csv.writer(DT, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        dt_writer.writerow(header_list)
        dt_writer.writerows(ll)

    with open('DT2.csv') as DT:
        dt_writer = csv.reader(DT, delimiter=',')
        counter = 0
        for row in dt_writer:
            counter += 1
            # print(row)
        print(counter)

    del titles_c_list
    del titles_d_list
    # del onehot_ner1
    del onehot_ner2

    # with open('ne_key.data', 'wb') as filehandle:
    #     # store the data as binary data stream
    #     pickle.dump(ne_key, filehandle)

    t2 = time.time()
    print(t2-t1)
    print(ne_key)