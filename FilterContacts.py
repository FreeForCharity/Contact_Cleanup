#!/usr/bin/env python3

import csv
import sys

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

with open(inputFilename, "r") as inFile, open(passFilename, "w") as passFile, open(failFilename, "w") as failFile:
    inCSV = csv.DictReader(inFile)
    passCSV = csv.DictWriter(passFile, fieldnames = outputFields)
    failCSV = csv.DictWriter(failFile, fieldnames = inCSV.fieldnames)

    passCSV.writeheader()
    failCSV.writeheader()

    for row in inCSV:
        #check if all name fields are empty, fail them if they are
        if(not(row["First Name"] or row["Middle Name"] or row["Last Name"])):
            failCSV.writerow(row)
            continue