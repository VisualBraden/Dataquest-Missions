## 2. Introduction To The Data ##

import pandas as pd
unrate = pd.read_csv("unrate.csv")

unrate["DATE"] = pd.to_datetime(unrate["DATE"])

print(unrate.head(12))