## 2. Frequency Distribution ##

fandango_distribution = norm_reviews.loc[:, "Fandango_Ratingvalue"].value_counts().sort_index()
imdb_distribution = norm_reviews.loc[:, "IMDB_norm"].value_counts().sort_index()
print(fandango_distribution, imdb_distribution)

## 4. Histogram In Matplotlib ##

fig, ax = plt.subplots()

ax.hist(norm_reviews.loc[:, "Fandango_Ratingvalue"], range=(0,5))
plt.show()

## 5. Comparing histograms ##

fig = plt.figure(figsize=(5,20))
ax1 = fig.add_subplot(4,1,1)
ax2 = fig.add_subplot(4,1,2)
ax3 = fig.add_subplot(4,1,3)
ax4 = fig.add_subplot(4,1,4)

ax1.hist(norm_reviews.loc[:, "Fandango_Ratingvalue"], 20, range=(0,5))
ax1.set(title="Distribution of Fandango Ratings", ylim=(0,50))

ax2.hist(norm_reviews.loc[:, "RT_user_norm"], 20, range=(0,5))
ax2.set(title="Distribution of Rotten Tomatoes Ratings", ylim=(0,50))

ax3.hist(norm_reviews.loc[:, "Metacritic_user_nom"], 20, range=(0,5))
ax3.set(title="Distribution of Metacritic Ratings", ylim=(0,50))

ax4.hist(norm_reviews.loc[:, "IMDB_norm"], 20, range=(0,5))
ax4.set(title="Distribution of IMDB Ratings", ylim=(0,50))


## 7. Box Plot ##

fig, ax = plt.subplots()
ax.boxplot(norm_reviews['RT_user_norm'])
ax.set_xticklabels(["Rotten Tomatoes"])
ax.set(ylim=(0,5))
plt.show()

## 8. Multiple Box Plots ##

num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']
fig, ax = plt.subplots()
ax.boxplot(norm_reviews[num_cols].values)
ax.set_xticklabels(num_cols, rotation=90)
ax.set(ylim=(0,5))
plt.show()