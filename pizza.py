#Pizza
import os
import json
import pandas
import numpy
import scipy
from itertools import islice
os.chdir("C:/Users/curious/Documents/TSINGHUA UNIVERSITY/Machine Learning/Pizza/")
def get_data():
    with open("test.json") as json_file:
        data = pandas.read_json(json_file)
        #Selecting out the second line of the dataFRAME
        #print(data.iloc[[2]])

        #Try others
        #print(data.loc[[2]])

        #Columns
        #print(data[['request_title']])

        #Get column names
        #print(list(data.columns.values))

        return data
get_data()

import numpy as np
import lda

def lda(x,n,iter,top):
    #x is the dataset,in corpus format(bag of words)
    #n is the number of topics wanted
    #iter is the number of iterations
    #top is the top number of words wanted in each topic(relavance)

    #vocab = lda.datasets.load_reuters_vocab()
    #titles = lda.datasets.load_reuters_titles()

    model = lda.LDA(n_topics = n, n_iter=iter, random_state=1)
    model.fit(x)
    topic_word = model.topic_word_
    n_top_words = top
    for i, topic_dist in enumerate(topic_word):
        topic_words = np.array(vocab)[np.argsort(topic_dist)][:-n_top_words:-1]
        print('Topic {}: {}'.format(i,' '.join(topic_words)))

    doc_topic = model.doc_topic_
    for i in range(10):
        print("{} (top topic: {})".format(titles[i], doc_topic[i].argmax()))



#For LDA, we may need to separate out into successful & unsuccessful datasets to draw out topics
