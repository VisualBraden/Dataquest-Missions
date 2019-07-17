## 2. Frequency Distribution ##

fandango_distribution = norm_reviews.loc[:, "Fandango_Ratingvalue"].value_counts().sort_index()
imdb_distribution = norm_reviews.loc[:, "IMDB_norm"].value_counts().sort_index()
print(fandango_distribution, imdb_distribution)

## 4. Histogram In Matplotlib ##

fig, ax = plt.subplots()

ax.hist(norm_reviews.loc[:, "Fandango_Ratingvalue"], range=(0,5))
plt.show()