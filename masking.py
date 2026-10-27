IP_PATROON = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
HOST_PATROON = IP_PATROON + r'(?:\.[A-Za-z0-9-]+)+'

def maskeer(regels):
    regels = regels.str.replace(HOST_PATROON, '<HOST>', regex=True)
    return regels.str.replace(IP_PATROON, '<IP>', regex=True)