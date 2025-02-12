import pandas as pd
import requests
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# import seaborn as sns

patch = "https://raw.githubusercontent.com/aiedu-courses/all_datasets/main/CrabeAge.csv"
data = requests.get(url=patch).text
data = data.split("\r\n")
result = list()
for e, line in enumerate(data):
    if bool(line):

        r = list()
        res = line.split(",")
        for i in res:
            try:
                a = float(i)
                r.append(a)
            except:
                r.append(i)

        result.append(r)
# print(result)

df = pd.DataFrame(result)
if __name__ == "__main__":
    print(df.head())
    print(df.shape)
    # print(len(df))
    # print(df.info())
    #
    # print(df.columns.tolist())
    #
    # X = df.drop([0, 8], axis=1)  # матрица объект-признак
    # y = df[8]  # target
    # #
    # print(X.head())
