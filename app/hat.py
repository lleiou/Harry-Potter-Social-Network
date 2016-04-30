import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from bs4 import BeautifulSoup
import re
import nltk
train = pd.read_csv('static/csv/sorting_hat2.csv')
feature = pd.DataFrame(np.zeros(shape=(len(train),26+1+1+26+26)))
ab = 'abcdefghijklmnopqrstuvwxyz'
for i in feature.index:
    feature.iloc[i,26] = train.loc[i,'birth']
    feature.iloc[i,27] = train.loc[i,'gender']
    for char in ab:
        feature.iloc[i,ab.index(char)] = train.loc[i,'name'].lower().count(char)
        feature.iloc[i,28+ab.index(char)] = train.loc[i,'hair'].lower().count(char)
        feature.iloc[i,54+ab.index(char)] = train.loc[i,'eye'].lower().count(char)
y = [1,3,4,2,1,4,2,1,3,1,3,1,3]
model = RandomForestClassifier(n_estimators=500)
model.fit(feature.values, y)
y_test = model.predict(feature.values)
f = np.zeros(26+1+1+26+26)
f[26] = 12
f[27] = 1
name = "name name"
hair = "black"
eye = "brown"
print("c")
for char in ab:
	f[ab.index(char)] = name.lower().count(char)
	f[28+ab.index(char)] = hair.lower().count(char)
	f[54+ab.index(char)] = eye.lower().count(char)
print("d")
data = [{"house": model.predict(f)}]
with open('static/js/data.json','w') as f:
	json.dump(data,f, ensure_ascii = False, encoding = 'utf-8')	