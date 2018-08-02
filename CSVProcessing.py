#!/usr/bin/env python3

import re

#Returns true if all specified fields are blank
def checkEmptyFields(fields, row):
    for field in fields:
        if(row[field]):
            return False

    return True

#Removes anything contained within parenthesis and puts it into the Notes field
def stripNotes(fields, row):
    for field in fields:
        matches = re.findall(r'\([^)]*\)', row[field])
        row[field] = re.sub(r'\([^)]*\)', "", row[field])
        for match in matches:
            row["Notes"] += "\n" + match

#Return the value stored in the first non-empty field
def extractFirstField(fields, row):
    for field in fields:
        if(row[field]):
            return row[field]
    
    return ""

#Validate phone numbers, only numbers between 10 and 14 characters long are valid
def validatePhone(fields, row):
    for field in fields:
        num = re.sub(r'[^\+?\d]', "", row[field])
        match = re.match(r'^\+?\d{10,14}$', num)
        if match:
            row[field] = match[0]
        else:
            if row[field]:
                row["Notes"] += "\nINVALID PHONE: " + row[field]
            row[field] = ''

