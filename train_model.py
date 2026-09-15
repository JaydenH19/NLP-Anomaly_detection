import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
from sklearn.model_selection import train_test_split

X = joblib.load('Data/IF_X.pkl')

df = pd.read_csv('Data/cleaned.csv')
suspicious = df['content'].str.contains('Failed|Invalid|BREAK-IN', case=False, na=False)
print(suspicious.sum())
print(len(df))

clf = IsolationForest(random_state=2, contamination=0.38) 

X_train, X_test, y_train, y_test, df_train, df_test = train_test_split(
    X, suspicious, df, test_size=0.33, random_state=42)


clf.fit(X_train)

decision_scores = clf.decision_function(X_test)
print("Decision Scores:", decision_scores)

y_pred = clf.predict(X_test)
print((y_pred == -1)) 

is_anomaly = y_pred == -1
print(df_test[is_anomaly])