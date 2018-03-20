import pandas as pd
from collections import Counter
from q01_create_dict.build import q01_create_dict


path = 'data/babies_name.csv'
data = pd.read_csv(path,names=['Name', 'Gender', 'Count', 'Year'])

def q02_top_names():
    "write your solution here"

