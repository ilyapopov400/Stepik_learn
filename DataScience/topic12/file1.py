import pandas as pd
from sklearn.datasets import fetch_california_housing

df = pd.read_csv("revexp.csv")
# X = df.drop(labels='expenditure', axis=1)
# y = df.drop('rate')


if __name__ == "__main__":
    print(df)
