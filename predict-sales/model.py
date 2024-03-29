import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from pathlib import Path

csv_path = '/sales.csv'
alt_csv_path = 'sales.csv'

default_path = Path(csv_path)

if default_path.is_file():
    dataset = pd.read_csv(csv_path)
else:
    dataset = pd.read_csv(alt_csv_path) 

# dataset = pd.read_csv('/sales.csv')

dataset['rate'].fillna(0, inplace=True)

dataset['sales_in_first_month'].fillna(dataset['sales_in_first_month'].mean(), inplace=True)

X = dataset.iloc[:, :3]

def convert_to_int(word):
    word_dict = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8,
                'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'zero':0, 0: 0}
    return word_dict[word]

X['rate'] = X['rate'].apply(lambda x : convert_to_int(x))

y = dataset.iloc[:, -1]

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

regressor.fit(X, y)

pickle.dump(regressor, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))
print(model.predict([[4, 300, 500]]))