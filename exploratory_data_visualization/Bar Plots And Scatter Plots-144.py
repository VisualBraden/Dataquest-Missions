## 2. Introduction to the data ##

import pandas as pd

reviews = pd.read_csv('fandango_scores.csv')
norm_list = ['FILM', 'RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
norm_reviews = reviews.loc[:,norm_list]
norm_reviews

## 4. Creating Bars ##

import matplotlib.pyplot as plt
from numpy import arange
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']

bar_heights = norm_reviews[num_cols].iloc[0].values
bar_positions = arange(5) + 0.75

fig, ax = plt.subplots()
ax.bar(bar_positions, bar_heights, 0.5)
plt.show()