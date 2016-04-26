#input a square matrix, and return a data frame with every row representing a pair, and columns representing the features:

import numpy as np
import pandas as pd

co_app = pd.read_csv('book_1_co_occurrence.csv',index_col=0)
label = pd.read_csv('WeasleyLabel1.csv',index_col=0)
#calculate the number of pairs;
num = len(co_app)*(len(co_app)-1)
X = pd.DataFrame(index = range(num), columns=range(3))
y = np.repeat(0,num)
n = np.shape(co_app)[0]

for i in range(len(co_app.index)-1):
    for j in range(i+1,n):
        X.iloc[i*(2*n-i-1)/2+(j-i)-1,0] = co_app.iloc[i,j]
        
polar = pd.read_csv('book_1_polarity.csv',index_col=0)
for i in range(len(polar.index) - 1):
    for j in range(i + 1, n):
        X.iloc[i * (2 * n - i - 1) / 2 + (j - i) - 1, 1] = co_app.iloc[i, j]
        
subj = pd.read_csv('book_1_subjectivity.csv', index_col=0)
for i in range(len(subj.index) - 1):
    for j in range(i + 1, n):
        X.iloc[i * (2 * n - i - 1) / 2 + (j - i) - 1, 2] = co_app.iloc[i, j]
        
for i in range(len(label.index) - 1):
    for j in range(i + 1, n):
        y[i * (2 * n - i - 1) / 2 + (j - i) - 1] = label.iloc[i, j]
