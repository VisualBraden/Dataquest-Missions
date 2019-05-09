## 1. Introducing Data Cleaning ##

# Read the text on the left, and then scroll to the bottom
# to find the instructions for the coding exercise

# Write your answer to the instructions below -- the list of
# lists is stored using the variable name `moma`

num_rows = len(moma)


## 2. Reading our MoMA Data Set ##



# Write your code here

from csv import reader
opened_file = open('artworks.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]


## 3. Replacing Substrings with the replace Method ##

age1 = "I am thirty-one years old"

age2 = age1.replace("thirty-one", "thirty-two")

## 4. Cleaning the Nationality and Gender Columns ##

# Variables you create in previous screens
# are available to you, so you don't need
# to read the CSV again
print(moma[1])
for row in moma:
    nationality = row[2]
    nationality = nationality.replace("(", "")
    nationality = nationality.replace(")", "")
    row[2] = nationality


for row in moma:
    gender = row[5]
    gender = gender.replace("(", "")
    gender = gender.replace(")", "")
    row[5] = gender
    
print(moma[1])

## 5. String Capitalization ##

for row in moma:
    gender = row[5]
    gender = gender.title()
    
    if gender == "":
        gender = "Gender Unknown/Other"
    row[5] = gender


for row in moma:
    nationality = row[2]
    nationality = nationality.title()
    
    if not nationality:
        nationality = "Nationality Unknown"
    row[2] = nationality

## 6. Errors During Data Cleaning ##

def clean_and_convert(date):
    # check that we don't have an empty string
    if date != "":
        # move the rest of the function inside
        # the if statement
        date = date.replace("(", "")
        date = date.replace(")", "")
        date = int(date)
    return date

for row in moma:
    begin = row[3]
    end = row[4]
    begin = clean_and_convert(begin)
    end = clean_and_convert(end)
    row[3] = begin
    row[4] = end
    

## 7. Parsing Numbers from Complex Strings, Part One ##

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for char in bad_chars:
            if char in string:
                string = string.replace(char, "")
    return string

stripped_test_data = []

for item in test_data:
    cleaned_item = strip_characters(item)
    stripped_test_data.append(cleaned_item)
    


## 8. Parsing Numbers from Complex Strings, Part Two ##

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    return string

stripped_test_data = ['1912', '1929', '1913-1923',
                      '1951', '1994', '1934',
                      '1915', '1995', '1912',
                      '1988', '2002', '1957-1959',
                      '1955', '1970', '1990-1999']

def process_date(date_str):
    if "-" in date_str:
        split_date = date_str.split("-")
        start = split_date[0]
        end = split_date[1]
        start = int(start)
        end = int(end)
        date_str = round(((start+end)/2))
    else:
        date_str = int(date_str)
    
    return date_str

processed_test_data = []

for item in stripped_test_data:
    date = process_date(item)
    processed_test_data.append(date)
    
for row in moma:
    date = row[6]
    date = strip_characters(date)
    date = process_date(date)
    row[6] = date

    
    
    
    
    
    