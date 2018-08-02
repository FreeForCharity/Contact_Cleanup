#!/usr/bin/env python3

import re

def checkEmptyFields(fields, row):
    for field in fields:
        if(row[field]):
            return False

    return True
    