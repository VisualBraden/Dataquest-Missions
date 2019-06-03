## 2. Introduction To The Data ##

import pandas as pd
unrate = pd.read_csv("unrate.csv")

unrate["DATE"] = pd.to_datetime(unrate["DATE"])

print(unrate.head(12))

## 6. Introduction to Matplotlib ##

import matplotlib.pyplot as plt

plt.plot()
plt.show()