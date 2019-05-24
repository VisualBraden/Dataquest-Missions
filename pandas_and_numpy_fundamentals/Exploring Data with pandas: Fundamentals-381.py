## 1. Introduction to the Data ##

f500_head = f500.head(10)
f500.info()

## 2. Vectorized Operations ##

rank_change = f500["rank"] - f500["previous_rank"] 

## 3. Series Data Exploration Methods ##

rank_change = f500["rank"] - f500['previous_rank']

rank_change_max = rank_change.max()

rank_change_min = rank_change.min()

## 4. Series Describe Method ##

rank = f500["rank"]
rank_desc = rank.describe()

prev_rank = f500["previous_rank"]
prev_rank_desc = prev_rank.describe()

## 5. Method Chaining ##

zero_previous_rank = f500["previous_rank"].value_counts().loc[0]