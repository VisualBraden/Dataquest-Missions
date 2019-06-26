## 2. Introduction to the data ##

import pandas as pd

reviews = pd.read_csv('fandango_scores.csv')
norm_list = ['FILM', 'RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
norm_reviews = reviews.loc[:,norm_list]
norm_reviews