## 1. Introduction ##

from csv import reader

opened_file = open("potus_visitors_2015.csv")
read_file = reader(opened_file)
potus = list(read_file)
potus = potus[1:]

## 3. The Datetime Module ##

import datetime as dt

## 4. The Datetime Class ##

import datetime as dt

ibm_founded = dt.datetime(1911,6,16)
man_on_moon = dt.datetime(1969,7,20,20,17)

## 5. Using Strptime to Parse Strings as Dates ##

# The `potus` list of lists is available from
# the earlier screen where we created it

date_format = '%m/%d/%y %H:%M'
# test format template on single date
test_date = (potus[2][2])
formatted_test = dt.datetime.strptime(test_date, date_format)
print(test_date)
print(type(formatted_test))
print(formatted_test)

#convert appt_start_date to datetime format
for row in potus:
    appt = row[2]
    appt = dt.datetime.strptime(appt, date_format)
    row[2] = appt 