# README sprint 3 - NLP Anomaly detection

NLP anomaly detection

## Gegevens student

Naam: Jayden Herbrink
Studentnummer: 97096023

## Wat ga ik bouwen?

Ik ga een heatmap maken voor de confusion matrix zodat ik niet alleen de getallen heb maar ook een visueel beeld erbij heb. Ook ga ik een staaf diagram maken zodat ik duidelijk kan zien hoeveel regels het model als anomalie markeert en hoeveel het er echt zijn (volgens suspicious die niet accuraat is omdat ik worden gebruik en niet gelabelde data).

## Waarom wil ik dit doen?

Zodat ik een duidelijk overzicht heb wat het model zegt en wat de waarheid is. Dat is duidelijker dan alleen getallen

## Randvoorwaarden

Dit project gebruikt echte SSH logs dus ik moet rekening houden met de AVG regels omdat ik IP-adressen zie.
Ik ga de IP adressen maskeren als IP of gedeeltelijk afgeschermd, zodat de anomalie zichtbaar blijft zonder een herleidbaar adres
te tonen

### Maatschappelijke impact

Dat je sneller doorhebt dat er een poging tot inbraak wordt gedaan en dat je er sneller op kan handelen om de gegevens van andere mensen te beschermen. Het risico is dat het een Ai model is en die kunnen fouten maken. de fouten kunnen false positives en gemiste detecties (false negatives).

### Randvoorwaarden voor deze sprint

Ik moet ervoor zorgen dat de IP adressen gemaskeerd zijn zodat het voldoet aan de AVG. Ook moet ik duidelijk aantonen dat het model een lage precision en recall heeft(~10%) dus dat het niet accuraat is.

### Wettelijke impact

Voor dit schoolproject is de AVG de belangrijkste wettelijke kader, vanwege de IP-adressen in de logdata.

#### Bron [Link naar de data die ik heb gebruikt om dit project te maken](https://github.com/logpai/loghub)

De LOGHUB dataset is vrij te gebruiken voor research en academisch werk. Dit schoolproject valt daaronder.
Bij gebruik moet verwezen worden naar de bron, vandaar de link hierboven naar de LOGHUB GitHub repository.

## Begin- en einddatum

Startdatum: 29 september 2026
Einddatum: 6 oktober 2026

## Leerdoelen

Mijn leerdoelen voor dit project zijn:

Ik wil leren werken met matplotlib en seaborn
Ik wil het resultaat kunnen uitleggen

## Werkprocessen

B1-K1-W1 Stemt opdracht af, plant werkzaamheden en bewaakt
de voortgang
B1-K1-W2 Maakt een technisch ontwerp voor software
B1-K1-W3 Realiseert (onderdelen van) software
B1-K1-W4 Test software
B1-K1-W5 Doet verbetervoorstellen voor de software
