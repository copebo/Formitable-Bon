# Formitable Reserveringupdate (geprint)
Nieuwe reserveringen van de huidige dag, uitdraaien op de bonnenprinter (bijv. in de keuken)

## Opzetten van lokale omgeving
Dit script maakt gebruik van:
 
**Python escpos**
```bash
pip install python-escpos
```

**Python dotenv**
```bash
pip install -U python-dotenv
```

### Omgevingsvariabele
Maak een bestand aan genaamd `.env` 
Vul dit document met de volgende variabele:

```bash
INTERVAL_MINUTEN=15
FORMITABLE_APIKEY=""
FORMITABLE_RESTAURANTID=""
IP_PRINTER=""
```

- De interval wordt gebruikt om te bepalen hoevaak de reserveringupdate afgedrukt moet worden (in minuten)
- De Formitable ApiKey is om een verbinding op te zetten met jouw account bij Formitable
- De Formitable RestaurantID is nodig om de gegevens van jouw restaurant op te halen
- IP Printer is het IP-adres van de printer waarop de update afgedrukt moet worden

