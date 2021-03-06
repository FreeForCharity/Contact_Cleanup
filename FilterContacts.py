#!/usr/bin/env python3

import csv
import sys

import CSVProcessing as process

if(len(sys.argv) == 1):
    inputFilename = "contacts.csv"
    passFilename = "pass.csv"
    failFilename = "fail.csv"
elif(len(sys.argv) == 4):
    inputFilename = sys.argv[0]
    passFilename = sys.argv[1]
    failFilename = sys.argv[2]
else:
    print("Invalid number of arguments")
    sys.exit(1)

outputFields = ["First Name", "Middle Name", "Last Name", "Title", "Primary Email", "Primary Phone", "Street", "City", "State", "Postal Code", "Notes"]

nameFields = ["First Name", "Middle Name", "Last Name"]

phoneFields = ["Primary Phone", "Home Phone", "Home Phone 2", "Mobile Phone"]
emailFields = ["E-mail Address", "E-mail 2 Address", "E-mail 3 Address"]
contactFields = phoneFields + emailFields

streetFields = ["Home Street", "Home Street 2", "Home Street 3"]

with open(inputFilename, "r") as inFile, open(passFilename, "w") as passFile, open(failFilename, "w") as failFile:
    inCSV = csv.DictReader(inFile)
    passCSV = csv.DictWriter(passFile, fieldnames = outputFields, extrasaction="ignore")
    failCSV = csv.DictWriter(failFile, fieldnames = inCSV.fieldnames, extrasaction="ignore")

    passCSV.writeheader()
    failCSV.writeheader()

    for row in inCSV:
        process.stripCR(inCSV.fieldnames, row)
        process.validatePhone(phoneFields, row)

        #check if all name fields are empty, fail them if they are
        if(process.checkEmptyFields(nameFields, row)):
            row["Notes"] += "\n(FAIL) NO NAME DATA"
            failCSV.writerow(row)
            continue

        #Check if we have contact info, fail them if we don't
        if(process.checkEmptyFields(contactFields, row)):
            row["Notes"] += "\n(FAIL) NO CONTACT DATA"
            failCSV.writerow(row)
            continue

        process.stripNotes(nameFields, row)
        row["Primary Email"] = process.extractFirstField(emailFields, row)
        row["Primary Phone"] = process.extractFirstField(phoneFields, row)

        row["Street"] = process.extractFirstField(streetFields, row)
        row["city"] = row["Home City"]
        row["State"] = row["Home State"]
        row["Postal Code"] = row["Home Postal Code"]
        row["County"] = row["Home Country"]

        passCSV.writerow(row)