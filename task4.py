import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("titles.csv")
stars = pd.read_csv("credits.csv")

data4 = data[['id', 'imdb_score', 'title']]
data4_sorted = data4.sort_values(by='imdb_score', ascending=False)
data5 = data4_sorted.head(1000)

actors = stars[['id', 'name', 'role']]
good_actor = actors[actors['role'] == 'ACTOR']
combined = good_actor.merge(data5)

actors_1 = combined["name"].unique()
actors_1_list = []
for i in actors_1:
    actors_1_list.append(len(combined[combined["name"] == i]))

data6 = pd.DataFrame(list(zip(actors_1, actors_1_list)), columns=['actors', 'amount'])
data7 = data6.sort_values(by='amount', ascending=False)
best = data7.head(10)
print(best)