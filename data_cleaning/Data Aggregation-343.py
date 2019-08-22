## 2. Introduction to the Data ##

import pandas as pd
import matplotlib 

happiness2015 = pd.read_csv("World_Happiness_2015.csv")
first_5 = happiness2015.head()
print(happiness2015.info())
