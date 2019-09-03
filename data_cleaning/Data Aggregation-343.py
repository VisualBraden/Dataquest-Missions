## 2. Introduction to the Data ##

import pandas as pd
import matplotlib 

happiness2015 = pd.read_csv("World_Happiness_2015.csv")
first_5 = happiness2015.head()
print(happiness2015.info())


## 3. Using Loops to Aggregate Data ##

mean_happiness = {}
regions = happiness2015['Region'].unique()

for x in regions:
    region_group = happiness2015[happiness2015['Region'] == x]
    mean_happiness[x] = region_group['Happiness Score'].mean()

## 5. Creating GroupBy Objects ##

grouped = happiness2015.groupby('Region')
aus_nz = grouped.get_group('Australia and New Zealand')