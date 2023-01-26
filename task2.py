import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("titles.csv")
# data.groupby('age_certification', dropna=False, suploads=True)[data['type'] == 'SHOW'].nunique().size().plot.pie(autopct='%1.2f%%')
data[data.type == 'SHOW'].groupby('age_certification', dropna=False).id.count().plot.pie(autopct='%1.2f%%')
# data.groupby('age_certification', dropna=False, suploads=True)[data['type'] == 'SHOW'].count().plot.pie(autopct='%1.2f%%')
# data[data.type = 'SHOW']

plt.show()