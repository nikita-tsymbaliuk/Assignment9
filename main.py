import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("titles.csv")

data['imdb_score'].hist()   #histogram
# data['imdb_score'].set_xlabel('bla')
# data['imdb_score'].set_ylabel('blu')
# data['imdb_score'].plot.pie()   #pie for all
# data['type'].count.plot.pie()
# data.groupby('type')['id'].count().plot.pie()
data.groupby('age_certification')['SHOW'].count().plot.pie(autopct='%1.2f%%')


plt.show()
pass
# import matplotlib.pyplot as plt
# import numpy as np