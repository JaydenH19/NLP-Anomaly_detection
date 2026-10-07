# Testverslag NLP anomaly detection

## Testscenario 1: train/test split

### Resultaat

De data die ik had werd goed gesplitst in 2 delen. Het ene deel was 33% en het andere deel was 67%. Ik heb een trainingsset gemaakt van 67%. Die bevat (train) 438.948 SSH-logs. Ik heb een testset gemaakt van 33%. Die bevat (test) 216.199 SSH-logs. De train- en testset maken samen 655.147 SSH-logs, dus het resultaat klopt.

### Vergelijking met verwachting

Dit was ook mijn verwachting. Bij train_test_split() in dashboard.py staat test_size=0.33, dus ik verwachtte dat de testset 33% is en de train set 67% van de 655.147 SSH logs zou zijn. In mijn testplan verwachtte ik dat de trainingsset iets groter zou zijn dan de testset. Het resultaat is preciezer: de trainingsset is 67% en dus ruim twee keer zo groot als de testset.

### Conclusie

De test is geslaagd. Tijdens het testen kreeg ik een foutmelding, omdat df 655.147 regels had en mijn filter uit de testset maar 216.199. Ik had df niet mee gesplitst. Ik heb df toegevoegd aan dezelfde train_test_split, zodat de tekst op dezelfde rijen bleef staan als de cijfers. Voortaan splits ik alles wat bij elkaar hoort tegelijk, zodat ik deze foutmelding niet nog een keer krijg.

## Testscenario 2: IP-maskering

### resultaat

### vergelijking met verwachting

### conclusie

## Testscenario 3: effect van proxy-aanpassingen

### REsultaat

### VErgelijking met verwachting

### COnclusie

## Eindconclusie en verbetervoorstellen