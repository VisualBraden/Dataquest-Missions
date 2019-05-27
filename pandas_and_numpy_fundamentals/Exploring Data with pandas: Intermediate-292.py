## 1. Introduction ##

import pandas as pd
# read the data set into a pandas dataframe
f500 = pd.read_csv("f500.csv", index_col=0)
f500.index.name = None

# replace 0 values in the "previous_rank" column with NaN
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan

f500_selection = f500[["rank","revenues","revenue_change"]].head(5)

## 2. Reading CSV files with pandas ##

f500 = pd.read_csv("f500.csv")
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan

## 3. Using iloc to select by integer position ##

fifth_row = f500.iloc[4]
company_value = f500.iloc[0,0]

## 4. Using iloc to select by integer position continued ##

first_three_rows = f500.iloc[0:3]
first_seventh_row_slice = f500.iloc[[0,6],0:5]


## 5. Using pandas methods to create boolean masks ##

null_bool = f500["previous_rank"].isnull()
null_previous_rank = f500[["company","rank", "previous_rank"]][null_bool]

## 6. Working with Integer Labels ##

null_previous_rank = f500[f500["previous_rank"].isnull()]
top5_null_prev_rank = null_previous_rank.iloc[0:5]

## 7. Pandas Index Alignment ##

previously_ranked = f500[f500["previous_rank"].notnull()]
rank_change = previously_ranked["previous_rank"] - previously_ranked["rank"]
f500["rank_change"] = rank_change

## 8. Using Boolean Operators ##

large_revenues = f500["revenues"]>100000
negative_profits = f500["profits"]<0
combined = large_revenues & negative_profits
big_rev_neg_profit = f500[combined]

## 9. Using Boolean Operators Continued ##

brazil_venezuela = f500[(f500["country"] == "Brazil") | (f500["country"] == "Venezuela")]

tech_outside_usa = f500[(f500["sector"] == "Technology") & (f500["country"] != "USA")].head(5)

## 10. Sorting Values ##

top_japanese_employer = f500[f500["country"]=="Japan"].sort_values("employees", ascending=False).iloc[0]

## 11. Using Loops with pandas ##

top_employer_by_country = {}

countries_arr = f500["country"].unique()

for c in countries_arr:
    employees_sort = f500[f500["country"]==c].sort_values("employees", ascending=False)
    top_employer = employees_sort.iloc[0]["company"]
    top_employer_by_country[c] = top_employer
    

## 12. Challenge: Calculating Return on Assets by Country ##

roa = f500.loc[:, "profits"] / f500.loc[:, "assets"]
f500["roa"] = roa

top_roa_by_sector = {}

sectors_unique = f500["sector"].unique()

for s in sectors_unique:
    selected = f500[f500["sector"]==s].sort_values("roa", ascending=False)
    top_roa_by_sector[s] = selected.iloc[0]["company"]