IP_PATROON = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

def maskeer(regels):
    return regels.str.replace(IP_PATROON, '<IP>', regex=True)
