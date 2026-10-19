# Testverslag NLP anomaly detection

## Testscenario 1: train/test split

### Resultaat

De data die ik had werd goed gesplitst in 2 delen. Het ene deel was 33% en het andere deel was 67%. Ik heb een trainingsset gemaakt van 67%. Die bevat (train) 438.948 SSH-logs. Ik heb een testset gemaakt van 33%. Die bevat (test) 216.199 SSH-logs. De train- en testset maken samen 655.147 SSH-logs, dus het resultaat klopt.

### Vergelijking met verwachting

Dit was ook mijn verwachting. Bij train_test_split() in dashboard.py staat test_size=0.33, dus ik verwachtte dat de testset 33% is en de train set 67% van de 655.147 SSH logs zou zijn. In mijn testplan verwachtte ik dat de trainingsset iets groter zou zijn dan de testset. Het resultaat is preciezer: de trainingsset is 67% en dus ruim twee keer zo groot als de testset.

### Conclusie

De test is geslaagd. Tijdens het testen kreeg ik een foutmelding, omdat df 655.147 regels had en mijn filter uit de testset maar 216.199. Ik had df niet mee gesplitst. Ik heb df toegevoegd aan dezelfde train_test_split, zodat de tekst op dezelfde rijen bleef staan als de cijfers. Voortaan splits ik alles wat bij elkaar hoort tegelijk, zodat ik deze foutmelding niet nog een keer krijg.

## Testscenario 2: IP-maskering (unit test)

### Resultaat

In de testset van 216.199 regels bevatten vóór de maskering 162.854 regels een IP-adres. Na de maskering met str.replace() waren dat er 0. Daarnaast heb ik een unit test geschreven met pytest test_masking.py met drie tests: een IP-adres wordt vervangen door `<IP>`, na de maskering is er geen IP-adres meer over, en een regel zonder IP blijft gelijk. Alle 3 de tests slaagden.

### Vergelijking met verwachting

Ik verwachtte vóór de maskering een getal groter dan 0 en erna precies 0. Dat klopt: 162.854 is ongeveer 75% van de testset, dus er waren echt IP-adressen om te maskeren. Zonder dat getal had "0" niets bewezen.

### Conclusie

De test is geslaagd. De maskering vervangt de IP-adressen zoals bedoeld, en de drie unit tests bevestigen dat. Er is wel een beperking: de test controleert alleen het patroon met vier groepen cijfers. In het dashboard bleef een hostnaam zoals `<IP>`.broad.xy.jx.dynamic.163data.com.cn staan. Die kan ook herleidbaar zijn, dus de regel is niet volledig geanonimiseerd. Een tweede beperking is dat test_masking.py het patroon kopieert uit dashboard.py, in plaats van de functie te importeren. Dat wil ik verbeteren.

## Testscenario 3: effect van proxy-aanpassingen (integratietest)

### Resultaat

Ik draaide het model met drie versies van suspicious. De rest liet ik gelijk (zelfde split en random_state, contamination=0.38).

| Versie | Verdachte regels | Precision | Recall | F1 |
| 1: `Failed\|Invalid\|BREAK-IN` | 246.619 (37,6%) | 10,4% | 10,5% | 10,5% |
| 2: + `authentication\|PAM\|Connection` | 586.104 (89,5%) | 99,99% | 42,4% | 59,5% |
| 3: + zinsdelen | 321.880 (49,1%) | 10,4% | 8,0% | 9,1% |

Bij versie 3 probeerde ik daarna contamination=0.49 (gelijk aan het percentage van suspicious). Dat gaf precision 23,8%, recall 23,4% en F1 23,6%.

### Vergelijking met verwachting

Ik verwachtte dat meer keywords de scores omhoog zouden brengen. Dat gebeurde alleen bij versie 2. Maar volgens mijn eigen slaagcriterium telt dat niet als verbetering, omdat 89,5% van alle regels "verdacht" werd. Bijna alles was dan verdacht, dus de hoge precision zegt niets meer. Versie 3 gaf geen verbetering (recall zakte). Bij contamination=0.49 gingen de scores omhoog omdat ik het model het verwachte percentage verraadde. Dat is geen eerlijke vergelijking, dus ik zette het terug op 0,38.

### Conclusie

Geen enkele versie voldeed aan mijn slaagcriterium. Mijn verwachting klopte dus niet, maar de test heeft zijn werk gedaan: ik zag dat een hogere score een oneerlijke meetlat kan verbergen. Het probleem zit waarschijnlijk niet in de keywords maar in het gebruik van een keyword-lijst als "waarheid". Daarnaast kwam ik erachter dat het model massale, herhaalde aanvallen mist: "Failed password for root" komt 176.784 keer voor, en door die aantallen lijken ze normaal voor TF-IDF met Isolation Forest.

## Eindconclusie en verbetervoorstellen

Scenario 1 en 2 zijn geslaagd. Scenario 3 bevestigde mijn verwachting niet, maar leverde wel het belangrijkste inzicht op: de `suspicious`-proxy is een zwakke ground truth.

Verbetervoorstellen:

1. De hostnaam na de IP-maskering ook maskeren.
2. maskeer() in een eigen bestand zetten, zodat dashboard en unit test dezelfde functie gebruiken.
3. Een geautomatiseerde test voor de train/test split (assert len(X_train) + len(X_test) == totaal).
4. Een betere ground truth, bijvoorbeeld zelf gelabelde synthetische aanvallen.
5. Een feature voor frequentie of IP, zodat massale herhaalde aanvallen opvallen.
6. Het staafdiagram laten rekenen met `cm[0][0]` enzovoort, in plaats van overgetypte getallen.
