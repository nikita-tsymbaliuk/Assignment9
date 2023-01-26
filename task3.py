import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("titles.csv")

# from datetime import datetime
# start_year = datetime(2000)
# end_year = datetime(2022)
# data_set[(start_year <= data_set.index) & (data_set.index <= end_year)].plot(grid=True)

# data >= 2000
data2 = data[data['release_year'] >= 2000]
data3 = data2[data['imdb_score'] >= 8][['release_year', 'imdb_score']]
data4 = data[data['release_year'] >= 2000][['release_year', 'imdb_score']]
data5 = data3.groupby('release_year').sum()
data6 = data4.groupby('release_year').sum()
data7 = (data5 / data6) * 100
data7.plot.bar().grid()
plt.title('% of successful movies for each year from 2000th')
plt.xlabel('years')
plt.ylabel('% of success')

print(data3)

plt.show()

########

#
# print(data3)
#
# plt.show()