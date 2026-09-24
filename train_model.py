import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix


X = joblib.load('Data/IF_X.pkl') # data in number

df = pd.read_csv('Data/cleaned.csv') # load readable tekst 
suspicious = df['content'].str.contains('Failed|Invalid|BREAK-IN|authentication|PAM|Connection', case=False, na=False) # True False array
print(suspicious.sum()) #print the True lines
print(len(df))

clf = IsolationForest(random_state=2, contamination=0.38) #makes untraind model 

X_train, X_test, y_train, y_test, df_train, df_test = train_test_split(
    X, suspicious, df, test_size=0.33, random_state=42) #makes training part and test part 

clf.fit(X_train) #Uses the training part to train the model

decision_scores = clf.decision_function(X_test) #calculates the score for each line
print("Decision Scores:", decision_scores)

y_pred = clf.predict(X_test) # makes -1 and 1 (-1 anomaly 1 normal)
print((y_pred == -1)) 

is_anomaly = y_pred == -1 #saves the True/False array in variabele
print(df_test[is_anomaly])

print("Precision:", precision_score(y_test, is_anomaly)) # print the Precision score (10.4%)
print("Recall:", recall_score(y_test, is_anomaly)) # print the Recall score (10.5%)
print("F1 score:", f1_score(y_test, is_anomaly)) # print the F1 score (10.5%) Going to fix it later to get higer scores. 

actual = y_test

predicted = is_anomaly

cm = confusion_matrix(actual, predicted)

print("confusion matrix: ", cm)

is_fp = is_anomaly & ~y_test 
print(df_test[is_fp])