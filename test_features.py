import pandas as pd
from features import bouw_tabel


def test_bouw_tabel_telt_per_ip_en_venster():
    regels = pd.Series([
        "Dec 12 00:53:17 LabSZ sshd[1]: Failed password for root from 1.2.3.4 port 100 ssh2",
        "Dec 12 00:53:20 LabSZ sshd[1]: Failed password for admin from 1.2.3.4 port 101 ssh2",
        "Dec 12 00:54:00 LabSZ sshd[1]: Failed password for root from 1.2.3.4 port 102 ssh2",
        "Dec 12 01:30:00 LabSZ sshd[1]: Connection closed by 5.6.7.8 [preauth]",
    ])
    tabel = bouw_tabel(regels)
    eerste = tabel[tabel['ip'] == '1.2.3.4'].iloc[0]
    assert len(tabel) == 2
    assert eerste['n_regels'] == 3
    assert eerste['n_poorten'] == 3
    assert eerste['n_gebruikers'] == 2
    assert eerste['n_mislukt'] == 3
    assert not eerste['verdacht']


def test_vijf_mislukte_pogingen_is_verdacht():
    regels = pd.Series([
        f"Dec 12 00:5{i}:00 LabSZ sshd[1]: Failed password for root from 1.2.3.4 port 10{i} ssh2"
        for i in range(5)
    ])
    tabel = bouw_tabel(regels)
    assert tabel.iloc[0]['n_mislukt'] == 5
    assert tabel.iloc[0]['verdacht']


def test_januari_hoort_bij_2016():
    regels = pd.Series([
        "Dec 31 23:59:00 LabSZ sshd[1]: Failed password for root from 1.2.3.4 port 100 ssh2",
        "Jan  1 00:01:00 LabSZ sshd[1]: Failed password for root from 1.2.3.4 port 101 ssh2",
    ])
    tabel = bouw_tabel(regels)
    assert tabel['tijdstip'].min().year == 2015
    assert tabel['tijdstip'].max().year == 2016