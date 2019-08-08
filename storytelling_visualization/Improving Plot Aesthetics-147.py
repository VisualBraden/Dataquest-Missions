## 3. Introduction To The Data ##

import pandas as pd
import matplotlib.pyplot as plt

women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
plt.plot(women_degrees['Year'], women_degrees['Biology'])
plt.show()

## 4. Visualizing The Gender Gap ##


men_degrees = 100 - (women_degrees)
men_degrees["Year"] = women_degrees["Year"]
year = men_degrees["Year"]
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(year, women_degrees["Biology"], c='b', label='Women')
ax.plot(year, men_degrees["Biology"], c='g', label='Men')
plt.title("Percentage of Biology Degrees Awarded By Gender")
plt.legend(loc="upper right")
plt.show()