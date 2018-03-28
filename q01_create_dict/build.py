import pandas as pd

path = 'data/babies_name.csv'
data = pd.read_csv(path,names=['Name', 'Gender', 'Count', 'Year'])
 
def q01_create_dict(data):
    return data[['Name','Count']].set_index('Name').to_dict()
