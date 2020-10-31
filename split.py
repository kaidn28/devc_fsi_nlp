import numpy as np
import pandas as pd

path = "./reviews.csv"
data = pd.read_csv(path)
print(data.head(10))
spliter = data.shape[0]*0.7
data_train = data.loc[:spliter]
data_test = data.loc[spliter:, "Review"]
data_test_labels = data.loc[spliter:, "Label"]
#print(data_train.head())
#print(data_test.head())
data_train.to_csv("./data_train.csv")
data_test_labels.to_csv("./data_test_labels.txt")
data_test.to_csv("./data_test.csv")
