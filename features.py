import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score

IP = r'(\d{1,3}(?:\.\d{1,3}){3})'
REGEL = r'^(\w{3})\s+(\d{1,2}) (\d{2}:\d{2}:\d{2}) \S+ sshd\[\d+\]: (.*)$'
GEBRUIKER = r'(?:[Ii]nvalid user|for(?: invalid user)?) (\S+) from'
MISLUKT = 'Failed password|Invalid user'
DREMPEL = 5


def bouw_tabel(regels):
    delen = regels.str.extract(REGEL)
    delen.columns = ['maand', 'dag', 'tijd', 'bericht']
    delen = delen.dropna()

    delen['jaar'] = delen['maand'].map(lambda m: '2015' if m == 'Dec' else '2016')
    delen['tijdstip'] = pd.to_datetime(
        delen['jaar'] + ' ' + delen['maand'] + ' ' + delen['dag'] + ' ' + delen['tijd'],
        format='%Y %b %d %H:%M:%S')
    delen['ip'] = delen['bericht'].str.findall(IP).str[-1]
    delen['poort'] = delen['bericht'].str.extract(r'port (\d+)')[0]
    delen['gebruiker'] = delen['bericht'].str.extract(GEBRUIKER)[0]
    delen['mislukt'] = delen['bericht'].str.contains(MISLUKT, case=False)
    delen = delen.dropna(subset=['ip'])

    tabel = delen.groupby(['ip', pd.Grouper(key='tijdstip', freq='5min')]).agg(
        n_regels=('bericht', 'size'),
        n_poorten=('poort', 'nunique'),
        n_gebruikers=('gebruiker', 'nunique'),
        n_mislukt=('mislukt', 'sum'),
    ).reset_index()
    tabel = tabel[tabel['n_regels'] > 0].copy()
    tabel['verdacht'] = tabel['n_mislukt'] >= DREMPEL
    return tabel


if __name__ == '__main__':
    with open('Data/SSH.log', errors='ignore') as f:
        regels = pd.Series(f.read().splitlines())

    tabel = bouw_tabel(regels)
    tabel['ip_nr'] = tabel['ip'].factorize()[0]
    aandeel = tabel['verdacht'].mean()

    print("Regels in het logbestand:", len(regels))
    print("Aantal rijen (IP + 5 minuten):", len(tabel))
    print("Label: verdacht = minstens", DREMPEL, "mislukte pogingen in 5 minuten")
    print("Aandeel verdacht:", round(aandeel, 3))
    if aandeel > 0.95 or aandeel < 0.05:
        print("LET OP: bijna alles of bijna niets is verdacht, dus de scores zeggen weinig.")
    print(tabel.drop(columns='ip').head())

    X = tabel[['n_poorten', 'n_gebruikers']]
    y = tabel['verdacht']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    print("Train:", len(X_train), "Test:", len(X_test))

    clf = IsolationForest(random_state=2, contamination=0.38)
    clf.fit(X_train)
    is_anomaly = clf.predict(X_test) == -1

    print("Precision:", precision_score(y_test, is_anomaly, zero_division=0))
    print("Recall:", recall_score(y_test, is_anomaly, zero_division=0))
    print("F1 score:", f1_score(y_test, is_anomaly, zero_division=0))