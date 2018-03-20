import pandas as pd
import numpy as np
from greyatomlib.babies_names_project.q03_top_in_each_year_1.build import q03_top_in_each_year_1
from collections import Counter

path = 'data/babies_name.csv'
data = pd.read_csv(path,names=['Name', 'Gender', 'Count', 'Year'])

def q04_top_in_each_year_2():
    "write your solution here"

