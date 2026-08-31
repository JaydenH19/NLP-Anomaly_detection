from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import joblib

df = pd.read_csv('Data/cleaned.csv')

vectorizer = TfidfVectorizer()
print(df['content'].isnull().sum())
df['content'] = df['content'].fillna('')
X = vectorizer.fit_transform(df['content'])
print(X.shape)

joblib.dump(vectorizer, 'Data/IF_vectorizer.pkl')
joblib.dump(X, 'Data/IF_X.pkl')