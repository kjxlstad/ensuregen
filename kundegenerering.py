#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import random
import csv

commonText = ["Registrert til", "Årlig forsikringspremie", "Dato opprettet", "Forsikringsbeløp", "Forsikringsbetingelser", "ForsikringsID"]

text = [["Kunder", ["Forsikringsnummer", "Etternavn", "Fornavn", "Kunde siden", "Fakturaadresse", "Ubetalte erstatninger"]],
        ["Batforsikring", commonText + ["Eier", "Registreringsnummer", "Type", "Modell", "Lengde i fot", "Årsmodell", "Motortype", "Motorstyrke (HP)"]],
        ["Hus- og innboforsikring", commonText + ["Forsikringsbeløp bygning", "Forsikringsbeløp innbo", "Adresse", "Byggeår", "Boligtype", "Boligmateriale", "Standard", "Kvadratmeter"]],
        ["Fritidsboligforsikring", commonText + ["Forsikringsbeløp bygning", "Forsikringsbeløp innbo", "Adresse", "Byggeår", "Boligtype", "Boligmateriale", "Standard", "Kvadratmeter"]],
        ["Reiseforsikringer", commonText + ["Premiumforsikring", "Forsikringssum"]],
        ["Skademeldinger", ["Registrert til", "Dato for skade", "Type skade", "Beksirvelse av skade", "Takseringsbeløp", "Utbetalt erstatnignsbeløp", "Skadenummer"]],
        ["Vitner", ["Registrert til", "Tilhører skadenummer", "Etternavn", "Fornavn", "Kontaktinformasjon"]]]

firstNames = []
surnames = []
adresses = []

with open ("names.csv", mode="r") as csvFile:
    csvReader = csv.reader(csvFile, delimiter = ",")
    lineCount = 0
    for row in csvReader:
        firstNames.append(row[0])
        surnames.append(row[1])
        adresses.append(row[4])

for adress in adresses:
    adresses[adresses.index(adress)] = ''.join([i for i in adress if not i.isdigit()])




seperator = ";"
numbersOfCustomers = 10000
numbersOfEach = 4000

skadenummerforvitner = []

def genCustomers(amount, writer):
    csvWriter.writerow([text[0][0]])
    csvWriter.writerow(text[0][1])
    for i in range(amount):
        row = []
        row.append(10000 + i)
        row.append(surnames[random.randint(0, 999)])
        row.append(firstNames[random.randint(0, 999)])
        row.append(genDate())
        row.append(adresses[random.randint(0, 999)] + str(random.randint(1, 100)))
        row.append(float(random.randint(0, 100000)))
        csvWriter.writerow(row)


def genInsurance(forsikringsNr):
    row = []
    row.append(forsikringsNr)
    row.append(float(random.randint(0, 10000)))
    row.append(genDate())
    row.append(float(random.randint(0, 10000)))
    row.append("asdf")
    row.append(200001 + forsikringsNr)
    return row

def genBoats(amount, csvWriter):
    global numbersOfCustomers
    csvWriter.writerow([text[1][0]])
    csvWriter.writerow(text[1][1])
    for i in range(amount):
        row = genInsurance(random.randint(0, numbersOfCustomers - 1) + 10000)
        row.append(surnames[random.randint(0, 999)] + "," + firstNames[random.randint(0, 999)])
        row.append("asdfasdf")
        row.append("agareg")
        row.append("asdf")
        row.append(random.randint(5, 35))
        row.append(random.randint(1960, 2019))
        row.append("dasdfasdf")
        row.append(random.randint(5, 200))
        csvWriter.writerow(row)

def genHouse(amount, csvWriter):
    global numbersOfCustomers
    csvWriter.writerow([text[2][0]])
    csvWriter.writerow(text[2][1])
    for i in range(amount):
        row = genInsurance(random.randint(0, numbersOfCustomers - 1) + 10000)
        row.append(float(random.randint(0, 100000)))
        row.append(float(random.randint(0, 100000)))
        row.append(adresses[random.randint(0, 999)] + str(random.randint(1, 100)))
        row.append(random.randint(1950, 2019))
        row.append("Enebolig")
        row.append("Treverk")
        row.append("NEK")
        row.append(random.randint(20, 500))
        csvWriter.writerow(row)

def genCabin(amount, csvWriter):
    global numbersOfCustomers
    csvWriter.writerow([text[3][0]])
    csvWriter.writerow(text[3][1])
    for i in range(amount):
        row = genInsurance(random.randint(0, numbersOfCustomers - 1) + 10000)
        row.append(float(random.randint(0, 100000)))
        row.append(float(random.randint(0, 100000)))
        row.append(adresses[random.randint(0, 999)] + str(random.randint(1, 100)))
        row.append(random.randint(1950, 2019))
        row.append("Enebolig")
        row.append("Treverk")
        row.append("NEK")
        row.append(random.randint(20, 500))
        csvWriter.writerow(row)

def genTravel(amount, csvWriter):
    global numbersOfCustomers
    csvWriter.writerow([text[4][0]])
    csvWriter.writerow(text[4][1])
    for i in range(amount):
        row = genInsurance(random.randint(0, numbersOfCustomers - 1) + 10000)
        row.append("true")
        row.append(float(random.randint(1000, 10000)))
        csvWriter.writerow(row)

def genStatement(amount, csvWriter):
    global numbersOfCustomers
    csvWriter.writerow([text[5][0]])
    csvWriter.writerow(text[5][1])
    for i in range(amount):
        row = []
        kundeid = random.randint(0, numbersOfCustomers - 1) + 10000
        skadeid = 100 + i
        row.append(kundeid)
        row.append(genDate())
        row.append("blala")
        row.append("Bla bla bla bla bla")
        row.append(random.randint(0, 100000))
        row.append(random.randint(0, 100000))
        row.append(skadeid)
        csvWriter.writerow(row)
        skadenummerforvitner.append([kundeid, skadeid])

def genVitner(amount, csvWriter):
    global numbersOfCustomers, numbersOfEach
    csvWriter.writerow([text[6][0]])
    csvWriter.writerow(text[6][1])
    for i in skadenummerforvitner:
        row = []
        row.append(i[0])
        row.append(i[1])
        row.append(surnames[random.randint(0, 999)])
        row.append(firstNames[random.randint(0, 999)])
        row.append(random.randint(22225555, 99999999))
        csvWriter.writerow(row)



def genDate():
    year = str(random.randint(1995, 2019))
    month = str(random.randint(1, 12))
    day = str(random.randint(1, 28))
    if len(month) == 1:
        month = "0" + month
    if len(day) == 1:
        day = "0" + day
    return year + "-" + month + "-" + day

with open("nyeKunder.csv", mode='wb') as csvFile:
    csvWriter = csv.writer(csvFile, delimiter = ";")

    csvWriter.writerow(["sep=;"])

    genCustomers(10000, csvWriter)
    genBoats(4000, csvWriter)
    genHouse(4000, csvWriter)
    genCabin(4000, csvWriter)
    genStatement(4000, csvWriter)
    genVitner(4000, csvWriter)


