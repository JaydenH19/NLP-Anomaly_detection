from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

df = pd.read_csv('Data/cleaned.csv')

vectorizer = TfidfVectorizer()
print(df['content'].isnull().sum())
df['content'] = df['content'].fillna('')
X = vectorizer.fit_transform(df['content'])
print(X.shape)