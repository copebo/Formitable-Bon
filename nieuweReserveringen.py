import requests

# Datum
import datetime
import locale
locale.setlocale(locale.LC_ALL, 'nl_NL')

# Printer benodigdheden
from escpos.constants import GS
from escpos.printer import Network
import six

# Env files
import os
from dotenv import load_dotenv
load_dotenv()

# Instellingen
intervalMinuten = int(os.getenv("INTERVAL_MINUTEN"))

# Datum van huidige dag
datumVandaag = datetime.datetime.now()
datumVandaagDatum = datumVandaag.strftime("%Y-%m-%d")
datumVandaagPrint = datumVandaag.strftime("%d-%m-%Y")
tijdVandaagPrint = datetime.datetime.now().strftime("%H:%M")

# Verbinding maken met Formitable API
restaurantID = os.getenv("FORMITABLE_RESTAURANTID")
aantalDagen = 1
response = requests.get(f"https://api.formitable.com/api/v1.2/{restaurantID}/booking/{datumVandaagDatum}/{aantalDagen}",
 headers={
   "ApiKey": os.getenv("FORMITABLE_APIKEY"),
   "Content-Type": "application/json",
   "Accept-Version": "v3"
 }
)

# Moment van opvragen - intervalMinuten
tijdSlotStart = datetime.datetime.now() - datetime.timedelta(minutes=intervalMinuten)

# Opvragen van reserveringen
reserveringen = response.json()

reserveringPrinten = []

# Reserveringen doorlopen
for reservering in reserveringen:

    # Moment van reserveren
    reserveringCreated = reservering["created"]
    reserveringCreated = datetime.datetime.strptime(reserveringCreated[:19], '%Y-%m-%dT%H:%M:%S')

    # Check of reservering nieuwer is dan intervalMinuten
    if reserveringCreated > tijdSlotStart:

        # Datum van het bezoek
        reserveringDatum = datetime.datetime.strptime(reservering["bookingDateTime"], '%Y-%m-%dT%H:%M:%S%z')
        reserveringTijd = ('%02d:%02d'%(reserveringDatum.hour,reserveringDatum.minute))

        if reservering['companyName']:
            reserveringNaam = reservering['companyName']
        else:
            if reservering['lastName']:
                reserveringNaam = reservering['lastName']
            else:
                reserveringNaam = reservering['firstName']

        if reservering['status'] == "ACCEPTED":
            reserveringTeken = "+"
        else:
            if reservering['status'] == "CANCELLED":
                reserveringTeken = "-"
            else:
                reserveringTeken = "?"

        reserveringPrinten.append(reserveringTeken+" "+ str(reservering['numberOfPeople']) + " p om "+ reserveringTijd +" - "+ reserveringNaam)

        for ticket in reservering['tickets']:
            if ticket["title"] == "High Tea":
                reserveringPrinten.append("^^ High Tea")

if reserveringPrinten:

    # print(""+ tijdVandaagPrint +" "+ datumVandaagPrint +"")
    # print(reserveringPrinten)

    # Lijstje opmaken om te printen
    kitchen = Network( os.getenv("IP_PRINTER") ) #Printer IP Address
    # kitchen.set(font='b')
    kitchen.text("Reservering Update ("+ tijdVandaagPrint +" "+ datumVandaagPrint +")\n\n")

    for reserveringPrint in reserveringPrinten:
        kitchen.text(reserveringPrint +"\n")

    # Cut
    kitchen._raw(b'\x1B\x64' + b'\x03')

