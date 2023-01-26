import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("titles.csv")
stars = pd.read_csv("credits.csv")

data5 = data[["id", "title", "genres", "imdb_score"]]
data5 = data5.sort_values(by="imdb_score", ascending=False)
data5 = data5.head(1000)
list_genres = []
for i in data5["genres"].unique():
    summary = 0
    word = ""
    for j in range(len(i)):
        summary += 1
        if i[summary] != "[" and i[summary] != "]" and i[summary] != "'" and i[summary] != "," and i[summary] != " ":
            word += i[summary]
        if i[summary] == " " and word != "":
            list_genres.append(word)
            word = ""
    else:
        # if word!="" or word!=" ":
        if word != "":
            list_genres.append(word)
        word = ""
data6 = pd.DataFrame({"genres": list_genres})
data6 = data6[data6["genres"] != ""]

genres = data6["genres"].unique()
amount_genres = []
for i in genres:
    amount_genres.append(len(data6[data6["genres"] == i]))

data7 = pd.DataFrame(list(zip(genres, amount_genres)), columns=['genres', 'amount'])
print(data7)
data7.plot(x="genres", y="amount", kind="bar").grid()
plt.title('Popularity of genres')
plt.xlabel('genres')
plt.ylabel('an amount of films')
plt.show()