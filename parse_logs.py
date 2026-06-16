import pandas as pd

line = []

with open('Data/SSH.log', 'r') as file:
    for lines in file:
        line.append(lines.strip())

df = pd.DataFrame(line, columns=['message'])  
print(df)
print(df.shape)