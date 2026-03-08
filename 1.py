# 1. Python ML Libraries
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

X = np.array([[1],[2],[3],[4],[5]])
y = np.array([2,4,5,4,5])
model = LinearRegression().fit(X, y)
print("LR prediction:", model.predict([[6]]))

iris_data = pd.DataFrame({'f1':[5.1,4.9,7.0,6.4],'f2':[3.5,3.0,3.2,3.2],'label':[0,0,1,1]})
clf = DecisionTreeClassifier().fit(iris_data[['f1','f2']], iris_data['label'])
print("DT prediction:", clf.predict([[6.0, 3.0]]))