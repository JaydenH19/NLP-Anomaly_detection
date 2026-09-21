# README sprint 2 - NLP Anomaly detection

NLP anomaly detection

## Gegevens student

Naam: Jayden Herbrink
Studentnummer: 97096023

## Wat ga ik bouwen?

Ik ga in deze sprint kijken hoe goed mijn Isolation Forest model daadwerkelijk is. Ik ga de precision, recall en F1-score berekenen om te zien hoeveel anomalieen het model correct herkent maar ook om te zien hoeveel hij mist en verkeerd markeerd. Ook ga ik een confusion matrix maken om een beeld te krijgen. Ook wil ik log regels kunnen laten zien die het model als anomalie heeft gemarkeerd

## Waarom wil ik dit doen?

Omdat ik niet weet hoe goed het model is. als ik die berekeningen niet doe dan kan ik niet garanderen dat het goed is en kan het zo zijn dat er een aanval lukt die veel impact gaat hebben op de maatschappij. Ook kan het zo zijn dat het model zegt dat het een anomalie is terwijl dat niet het geval is. Als dat gebeurt kan het zijn dat er iets van het internet gehaald wordt dat grote impact kan hebben

## Randvoorwaarden

Dit project gebruikt echte SSH logs dus ik moet rekening houden met de AVG regels omdat ik IP-adressen zie.
Ik ga de IP adressen maskeren als IP of gedeeltelijk afgeschermd, zodat de anomalie zichtbaar blijft zonder een herleidbaar adres
te tonen

### Maatschappelijke impact

Ik gebruik de suspicious die gebaseerd is op de woorden Failed, Invalid en BREAK-IN omdat ik geen label bestanden heb die geverifieerd door iemand die er verstand van heeft. Dit is een beperking sommige regels met deze woorden zijn mogelijk geen echte aanvallen (bijvoorbeeld een gebruiker die per ongeluk zijn wachtwoord verkeerd typt), en sommige echte aanvallen gebruiken misschien geen van deze woorden. Mijn precision/recall-resultaten moeten daarom niet gelezen worden als iets dat 100% klopt.

### Wettelijke impact

Voor dit schoolproject is de AVG de belangrijkste wettelijke kader, vanwege de IP-adressen in de logdata.

#### Bron [Link naar de data die ik heb gebruikt om dit project te maken](https://github.com/logpai/loghub)

De LOGHUB dataset is vrij te gebruiken voor research en academisch werk. Dit schoolproject valt daaronder.
Bij gebruik moet verwezen worden naar de bron, vandaar de link hierboven naar de LOGHUB GitHub repository.

## Begin- en einddatum

Startdatum: 23 september 2026
Einddatum: 30 september 2026

## Leerdoelen

Mijn leerdoelen voor dit project zijn:

Ik wil leren om goede naukeurige berekeningen te kunnen maken om mijn werk goed te kunnen doen.
Ik wil ook oefen berekeningen gaan maken om het goed onder de knie te krijgen. (niet echt een leerdoel maar iets wat ik ga doen. AI gaat de sommen bedenken en controleren voor mij.)
Ik wil Confusion Matrix begrijpen, lezen en uitleggen.

## Werkprocessen

B1-K1-W1 Stemt opdracht af, plant werkzaamheden en bewaakt
de voortgang
B1-K1-W2 Maakt een technisch ontwerp voor software
B1-K1-W3 Realiseert (onderdelen van) software
B1-K1-W4 Test software
B1-K1-W5 Doet verbetervoorstellen voor de software
