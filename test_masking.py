import pandas as pd

IP_PATROON = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

def maskeer(regels):
    return regels.str.replace(IP_PATROON, '<IP>', regex=True)

def test_ip_wordt_vervangen():
    regels = pd.Series(["Invalid user admin from 173.234.31.186"])
    resultaat = maskeer(regels)
    assert resultaat.iloc[0] == "Invalid user admin from <IP>"

def test_geen_ip_meer_over():
    regels = pd.Series(["Failed password for root from 5.188.10.182 port 52995 ssh2"])
    resultaat = maskeer(regels)
    assert not resultaat.str.contains(IP_PATROON, regex=True).any()

def test_regel_zonder_ip_blijft_gelijk():
    regels = pd.Series(["Connection closed [preauth]"])
    assert maskeer(regels).iloc[0] == "Connection closed [preauth]"