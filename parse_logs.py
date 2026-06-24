import pandas as pd

line = []

with open('Data/SSH.log', 'r') as file:
    for lines in file:
        line.append(lines.strip())

df = pd.DataFrame(line, columns=['message'])  
df ['content'] = df['message'].str.rsplit(":", n=1, expand=True)[1]


df['content'] = df['content'].str.strip()
df['content'].to_csv("Data/cleaned.csv", index=False)

print(df)
print(df.shape) 