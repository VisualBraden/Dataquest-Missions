## 1. Recap ##

import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv('unrate.csv')
unrate['DATE'] = pd.to_datetime(unrate['DATE'])

plt.plot(unrate['DATE'].head(12), unrate['VALUE'].head(12))
plt.xticks(rotation=90)
plt.xlabel("Month")
plt.ylabel("Unemployment Rate")
plt.title("Monthly Unemployment Trends, 1948")
plt.show()

## 3. Matplotlib Classes ##

import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
plt.show()

## 5. Adding Data ##

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot(unrate['DATE'].head(12), unrate['VALUE'].head(12))
ax2.plot(unrate.loc[12:23, 'DATE'], unrate.loc[12:23, 'VALUE'])

plt.show()

## 6. Formatting And Spacing ##

fig = plt.figure(figsize=(12,5))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot(unrate[0:12]['DATE'], unrate[0:12]['VALUE'])
ax1.set_title('Monthly Unemployment Rate, 1948')
ax2.plot(unrate[12:24]['DATE'], unrate[12:24]['VALUE'])
ax2.set_title('Monthly Unemployment Rate, 1949')
plt.show()

## 7. Comparing Across More Years ##

#create grid
fig = plt.figure(figsize=(12,12))
#instantiate axes objects
ax1 = fig.add_subplot(5,1,1)
ax2 = fig.add_subplot(5,1,2)
ax3 = fig.add_subplot(5,1,3)
ax4 = fig.add_subplot(5,1,4)
ax5 = fig.add_subplot(5,1,5)
# generate line plots
ax1.plot(unrate[0:12]['DATE'], unrate[0:12]['VALUE'])

ax2.plot(unrate[12:24]['DATE'], unrate[12:24]['VALUE'])

ax3.plot(unrate[24:36]['DATE'], unrate[24:36]['VALUE'])

ax4.plot(unrate[36:48]['DATE'], unrate[36:48]['VALUE'])

ax5.plot(unrate[48:60]['DATE'], unrate[48:60]['VALUE'])

plt.show()