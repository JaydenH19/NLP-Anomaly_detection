import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

X = joblib.load('Data/IF_X.pkl')

df = pd.read_csv('Data/cleaned.csv')
verdacht = df['content'].str.contains('Failed|Invalid|BREAK-IN', case=False, na=False)
print(verdacht.sum())
print(len(df))

clf = IsolationForest(contamination=0.38)
clf.fit(X)

y_pred = clf.predict(X)
print((y_pred == -1).sum())