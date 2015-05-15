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
        print(data.iloc[[2]])
        #Try others
        print(data.loc[[2]])
        return data
get_data()