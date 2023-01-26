import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("titles.csv")

# data['imdb_score'].hist()
scores_m = data[data['type'] == 'MOVIE']['imdb_score'].dropna()
scores_s = data[data['type'] == 'SHOW']['imdb_score'].dropna()
plt.hist(scores_m, np.arange(0, 10.2, 0.2))
plt.hist(scores_s, np.arange(0, 10.2, 0.2))
plt.title('Movies and Shows')
plt.xlabel('IMDB score')
plt.ylabel('an amount of votes')














# plt.set_xlabel('BLA')
# data.set_ylabel('ALB')
#grid bins 10 grades 0.2 krok 50 bins
# scores_s.grid()
# scores_m.grid()

plt.show()