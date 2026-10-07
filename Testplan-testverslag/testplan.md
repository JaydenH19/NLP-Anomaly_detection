# Testplan NLP anomaly detection

## Testscenario 1: train/test split (handmatige test)

### Wat ga ik precies testen?

Ik ga testen of de data goed gesplitst is in 2 delen. Een trainings set en een test set. De trainings set ga ik gebruiken om mijn model te trainen op het detecteren van anomalies. De test set wil ik gebruiken om het model te toetsen zodat ik kan kijken hoe het presteert als die de antwoorden nog niet weet.

### Hoe ga ik dit testen?

Ik ga dit testen door de lengte van de training en test set te printen en dan delen door het totaal aantal. Ik ga dit toevoegen direct na dat ik de 2 verschillende sets maak zodat ik het direct kan controleren. Ik vergelijk de som van beide met het totale aantal regels in de dataset (655.147), en ik controleer of de verhouding overeenkomt met de ingestelde test_size=0.33.

### Wat verwacht ik als resultaat?

Ik verwacht dat ik ik 2 verschillende sets krijg. 1 om te trainen en 1 om te toetsen. Ik verwacht dat ik een iets grotere training set heb dan test set omdat ik het model dan op meer data kan trainen en een kleiner set voor het testen. Ik verwacht dat er een bepaalde score/ getal uitkomt dat laat zien hoe groot de sets zijn.

### Hoe weet ik of de test is geslaagd?

Ik weet of de test geslaagd is door het gewenste resultaat te krijgen. Dus ik verwacht meerdere getallen terug te krijgen met hoe groot de training set is, de test set en ik verwacht dat de training set groter is dan de test set.

Train: 438.948 regels, Test: 216.199 regels. Samen 655.147, gelijk aan het totaal. De verhouding (67%/33%) komt overeen met de verwachting. Test geslaagd.

## Testscenario 2: IP-maskering (unit test)

### Wat ga ik precies testen?

Ik ga testen of de ip adressen goed worden verborgen zodat mijn project voldoet aan de avg regelgeving.

### Hoe ga ik dit testen?

Ik ga dit testen door het programma 2 keer te draaien 1 keer met: str.replace(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', '<IP>', regex=True) en 1 keer zonder zodat ik kan zien wat de verschillen zijn. Ik tel met str.contains(...).sum() hoeveel regels nog een IP-adres bevatten, één keer vóór en één keer na de maskering.

### Wat verwacht ik als resultaat?

Ik verwacht dat het aantal IP-adressen in df_test['content'] vóór de maskering groter is dan 0, omdat de SSH-logs echte IP-adressen bevatten. Na de maskering met str.replace() verwacht ik dat dit aantal precies 0 is.

### Hoe weet ik of de test geslaagd is?

De test is geslaagd als de telling vóór de maskering groter is dan 0 en de telling na de maskering precies 0 is. Is het getal na de maskering groter dan 0, dan is de test mislukt.

## Testscenario 3: effect van proxy-aanpassingen op precision/recall (integratietest)

### Wat ga ik precies testen?

Ik test of een andere keyword lijst (Failed|Invalid|BREAK-IN) voor suspicious het model echt beter laat presteren, of dat de scores alleen hoger lijken te worden doordat de meetlat verandert.

### Hoe ga ik dit testen?

Ik draai het model met drie versies van suspicious en vergelijk steeds het aantal verdachte regels, precision, recall en F1. De drie versies zijn: (1) Failed|Invalid|BREAK-IN, (2) uitgebreid met authentication|PAM|Connection, en (3) uitgebreid met zinsdelen zoals ignoring max retries en Too many authentication failures. De rest laat ik gelijk.

### Wat verwacht ik als resultaat?

Ik verwacht dat meer keywords de scores omhoog brengen, omdat suspicious dan beter aansluit op wat het model markeert.

### Hoe weet ik of de test geslaagd is?

Een versie telt alleen als verbetering als het percentage verdachte regels realistisch blijft (niet bijna alles) en ik contamination niet aanpas aan het percentage van suspicious. Een hogere score alleen is niet genoeg.
