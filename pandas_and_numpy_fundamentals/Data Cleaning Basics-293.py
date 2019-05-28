## 1. Reading CSV Files with Encodings ##

import pandas as pd
laptops = pd.read_csv("laptops.csv", encoding = "Latin-1")
laptops.info()

## 2. Cleaning Column Names ##

new_columns = []

for index in laptops.columns:
    new_columns.append(index.strip())

laptops.columns = new_columns

## 3. Cleaning Column Names Continued ##

import pandas as pd
laptops = pd.read_csv('laptops.csv', encoding='Latin-1')

def clean_index_columns(col):
    col = col.strip()
    col = col.replace("Operating System", "os")
    col = col.replace(" ", "_")
    col = col.replace("(", "")
    col = col.replace(")", "")
    col = col.lower()
    return col

new_columns = []

for c in laptops.columns:
    cleaned = clean_index_columns(c)
    new_columns.append(cleaned)

laptops.columns = new_columns