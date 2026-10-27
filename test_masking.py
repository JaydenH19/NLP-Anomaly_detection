import pandas as pd
from masking import maskeer, IP_PATROON

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

def test_hostnaam_met_ip_wordt_vervangen():
    regels = pd.Series(["reverse mapping checking getaddrinfo for 224.247.186.60.broad.hz.zj.dynamic.163data.com.cn [60.186.247.224] failed - POSSIBLE BREAK-IN ATTEMPT!"])
    resultaat = maskeer(regels)
    assert resultaat.iloc[0] == "reverse mapping checking getaddrinfo for <HOST> [<IP>] failed - POSSIBLE BREAK-IN ATTEMPT!"
    assert "163data" not in resultaat.iloc[0]

# pytest test_masking.py