# Formitable Reserveringupdate (geprint)
Nieuwe reserveringen van de huidige dag, uitdraaien op de bonnenprinter (bijv. in de keuken).
Dit script is opgebouwd voor de "Star SP742" en zal later uitgebreid worden.

## Opzetten van lokale omgeving
Dit script maakt gebruik van:
 
**Python (escpos)[https://github.com/python-escpos/python-escpos]**
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

### Handige links
- Epson ESC/POS commands https://reference.epson-biz.com/modules/ref_escpos/index.php?content_id=2
- 

## Cronjob op Raspberry
Om te zorgen dat het script niet alleen draait wanneer iemand het bestand aanroept, kan je eenvoudig een cronjob instellen op een Raspberry PI
```bash
crontab -e
```
Kies hierna voor nano als editor

`*/5 11-20 * * * /home/pi/Formitable-Bon/nieuweReserveringen.py` zorgt ervoor dat nieuweReserveringen.py elke dag van de week tussen 11-20 elke 5 minuten wordt aangeroepen

Uitrekenen kan via https://crontab.guru
