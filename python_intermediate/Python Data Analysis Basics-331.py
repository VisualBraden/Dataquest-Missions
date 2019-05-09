## 1. Reading our MoMA Data Set ##

from csv import reader

# Read the `artworks_clean.csv` file
opened_file = open('artworks_clean.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

# Convert the birthdate values
for row in moma:
    birth_date = row[3]
    if birth_date != "":
        birth_date = int(birth_date)
    row[3] = birth_date
    
# Convert the death date values
for row in moma:
    death_date = row[4]
    if death_date != "":
        death_date = int(death_date)
    row[4] = death_date

# Write your code below

for row in moma:
    date = row[6]
    if date != "":
        date = int(date)
    row[6] = date









## 2. Calculating Artist Ages ##

ages = []
for row in moma:
    date = row[6]
    birth = row[3]
    if birth != "":
        age = date - birth
    else:
        age = 0
    ages.append(age)

final_ages = []

for each in ages:
    if each > 20:
        final_age = each
    else:
        final_age = "Unknown"
    final_ages.append(final_age)
    


## 3. Converting Ages to Decades ##

# The ages variable is available
# from the previous screen        
decades = []

for item in ages:
    if item == "Unknown":
        decade = item
    else:
        decade = str(item)
        decade = decade[:-1]
        decade += "0s"
    decades.append(decade)

## 4. Summarizing the Decade Data ##

# The decades variable is available
# from the previous screen

decade_frequency = {}

for item in decades:
    if item not in decade_frequency:
        decade_frequency[item] = 1
    else:
        decade_frequency[item] += 1
        

## 5. Inserting Variables Into Strings ##

artist = "Pablo Picasso"
birth_year = 1881

template = "{name}'s birth year is {date}"

print(template.format(date=birth_year, name=artist))

## 6. Creating an Artist Frequency Table ##

artist_freq = {}

for row in moma:
    artist = row[1]
    if artist not in artist_freq:
        artist_freq[artist] = 1
    else:
        artist_freq[artist] += 1
        

## 7. Creating an Artist Summary Function ##

def artist_summary(artist):
    num_artworks = artist_freq[artist]
    template = "There are {num} artworks by {name} in the data set"
    print(template.format(num=num_artworks, name=artist))
    
    return

artist_summary("Henri Matisse")

## 8. Formatting Numbers Inside Strings ##

pop_millions = [
    ["China", 1379.302771],
    ["India", 1281.935991],
    ["USA",  326.625791],
    ["Indonesia",  260.580739],
    ["Brazil",  207.353391],
]

template = "The population of {country} is {pop:,.2f} million"

for item in pop_millions:
    country = item[0]
    pop = item[1]
    statement = template.format(country=country, pop=pop)
    print(statement)

## 9. Challenge: Summarizing Artwork Gender Data ##

#Create frequency table dictionary of the artworks organised by gender
#create empty dictionary
gender_freq = {}
# loop through moma to build the dictionary

for row in moma:
    gender = row[5]
    if gender in gender_freq:
        gender_freq[gender] += 1
    else:
        gender_freq[gender] = 1

for gen, freq in gender_freq.items():
    statement = "There are {:,} artworks by {} artists"
    print(statement.format(freq, gen))
