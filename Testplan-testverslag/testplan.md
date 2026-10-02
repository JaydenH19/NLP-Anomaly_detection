# Testplan NLP anomaly detection

## Testscenario 1: train/test split (unit test)

### Wat ga ik precies testen?

Ik ga testen of de data goed gesplitst is in 2 delen. Een trainings set en een test set. De trainings set ga ik gebruiken om mijn model te trainen op het detecteren van anomalies. De test set wil ik gebruiken om het model te toetsen zodat ik kan kijken hoe het presteert als die de antwoorden nog niet weet.

### Hoe ga ik dit testen?

Ik ga dit testen door de lengte van de training en test set te printen en dan delen door het totaal aantal ik ga dit toevoegen direct na dat ik de 2 verschillende sets maak zodat ik het direct kan controleren. Ik vergelijk de som van beide met het totale aantal regels in de dataset (655.147), en ik controleer of de verhouding overeenkomt met de ingestelde test_size=0.33.

### Wat verwacht ik als resultaat?

Ik verwacht dat ik ik 2 verschillende sets krijg. 1 om te trainen en 1 om te toetsen. Ik verwacht dat ik een iets grotere training set heb dan test set omdat ik het model dan op meer data kan trainen en een kleiner set voor het testen. Ik verwacht dat er een bepaalde score/ getal uitkomt dat laat zien hoe groot de sets zijn.

### Hoe weet ik of de test is geslaagd?

Ik weet of de test geslaagd is door het gewenste resultaat te krijgen. Dus ik verwacht meerdere getallen terug te krijgen met hoe groot de training set is, de test set en ik verwacht dat de training set groter is dan de test set.

Train: 438.948 regels, Test: 216.199 regels. Samen 655.147, gelijk aan het totaal. De verhouding (67%/33%) komt overeen met de verwachting. Test geslaagd.

## Testscenario 2: IP-maskering (unit test)
