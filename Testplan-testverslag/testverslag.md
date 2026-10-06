# Testverslag NLP anomaly detection

## Inleiding

(2-3 zinnen: wat is getest, wanneer, met welke omgeving)

## Testscenario 1: train/test split

### Resultaat

De data die ik had werd goed gesplitst in 2 delen. 1 deel was 33% en het andere deel was 67%. Ik heb een trainings set gemaakt van 67%. Die bevat (Train) 438.948 SSH logs. ik heb een test set gemaakt van 33%. Die bevat (Test) 216.199 SSH logs. de Train en test set maakt samen: 655.147 SSH logs dus het resultaat klopt.

### Vergelijking met verwachting

Dit was ook mijn verwachting. Als je kijk naar de code in dashboard.py en dan regel 22 en dan test_size=0.33 verwachte ik dat de test set 33% van de 655.147 SSH logs is.

### Conclusie

De test is geslaagd. Tijdens het testen kreeg ik een foutmelding, omdat df 655.147 regels had en mijn filter uit de testset maar 216.199. Ik had df niet mee gesplitst. Ik heb df toegevoegd aan dezelfde train_test_split, zodat de tekst op dezelfde rijen bleef staan als de cijfers. Voortaan splits ik alles wat bij elkaar hoort tegelijk zodat ik deze foutmelding niet nog een keer krijg.

## Testscenario 2: IP-maskering

### Resultaat

### Vergelijking met verwachting

### Conclusie

## Testscenario 3: effect van proxy-aanpassingen

### Resultaat

### Vergelijking met verwachting

### Conclusie

## Eindconclusie en verbetervoorstellen