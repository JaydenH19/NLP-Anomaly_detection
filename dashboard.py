import streamlit as st
import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Anomaly dashboard")

X = joblib.load('Data/IF_X.pkl') # data in number

df = pd.read_csv('Data/cleaned.csv') # load readable tekst 
suspicious = df['content'].str.contains('Failed|Invalid|BREAK-IN', case=False, na=False) # True False array
print(suspicious.sum()) #print the True lines
print(len(df))

clf = IsolationForest(random_state=2, contamination=0.38) #makes untraind model 

X_train, X_test, y_train, y_test, df_train, df_test = train_test_split(
    X, suspicious, df, test_size=0.33, random_state=42) #makes training part and test part 

print(len(y_train))
print(len(y_test))

clf.fit(X_train) #Uses the training part to train the model

decision_scores = clf.decision_function(X_test) #calculates the score for each line
print("Decision Scores:\n ", decision_scores)

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

plt.figure()
anomaly = ['True N', 'False P', 'False N', 'True P']
amount = [61360, 73455, 72846, 8538]
bar_labels = ['Right', 'Wrong']
bar_colors = ['tab:green', 'tab:red', 'tab:red', 'tab:green']

plt.bar(anomaly, amount, color=bar_colors, width=0.3)
plt.title('Anomaly')
plt.xlabel('Meaning')
plt.ylabel('amount')
plt.show()

print("\n confusion matrix: \n", cm)

print("\n False positive")
is_fp = is_anomaly & ~y_test # combine 2 conditions with &. 
print(df_test[is_fp]) # shows readeble Fasle positives

print("False Negative")
is_fn = y_test & ~is_anomaly #Same principle as above 
print(df_test[is_fn]) # False Negative

print("Aantal 'Failed password for root':", df['content'].str.contains('Failed password for root', case=False, na=False).sum())
#counts how often 'Failed password for root' is in the data set

print(df_test[is_fp].head(5)) #shows only the 5 first rows
print(df_test[is_fn].head(5))

@st.cache_resource
def train_model():
    import sklearn
    model = sklearn.svm.SVC()
    return model

my_model = train_model()
st.write("Precision:", precision_score(y_test, is_anomaly))
st.write("Recall:", recall_score(y_test, is_anomaly))
st.write("F1 score:", f1_score(y_test, is_anomaly))

col1, col2 = st.columns(2)

df_test['content'] = df_test['content'].str.replace(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', '<IP>', regex=True)
#mask the ip address to complie with the AVG laws

with col1:
    fig, ax = plt.subplots()
    sns.heatmap(cm,
                annot=True,
                fmt='g',
                xticklabels=['not anomaly','Anomaly'],
                yticklabels=['not anomaly','Anomaly'],
                ax=ax)
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots()
    ax.bar(anomaly, amount, color=bar_colors, width=0.3)
    ax.set_title('Anomaly')
    ax.set_xlabel('Meaning')
    ax.set_ylabel('amount')
    st.pyplot(fig)

st.subheader("Alle gemarkeerde anomalieën")
resultaten = df_test[is_anomaly].copy()
resultaten['score'] = decision_scores[is_anomaly]
resultaten = resultaten.sort_values('score')
st.dataframe(resultaten)

if st.button('Refresh Cache'):
    st.cache_data.clear()

#streamlit run dashboard.py