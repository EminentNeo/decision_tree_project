# %load q02_decision_regressor_plot/build.py
# default imports
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.switch_backend('agg')

data = pd.read_csv('./data/house_pricing.csv')
X = data.iloc[:, :-1]
y = data.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=9)

depth_list = [2, 8, 10, 15, 20, 25, 30, 35, 45, 50, 80]
def decision_regressor_plot(X_train,X_test,y_train,y_test,depths):
    train_scores = []
    test_scores = []
    for x in depth_list:
        dt = DecisionTreeRegressor(max_depth = x)
        dt.fit(X_train,y_train)
        y_pred = dt.predict(X_train)
        train_scores.append(mean_squared_error(y_train,y_pred))
        dt_1 = DecisionTreeRegressor(max_depth= x)
        dt_1.fit(X_train,y_train)
        y_pred_test = dt.predict(X_test)
        test_scores.append(mean_squared_error(y_test,y_pred_test))
        plt.plot(train_scores)
        plt.plot(test_scores)
        plt.xlabel('Depth')
        plt.ylabel('mean squared error')
        return
decision_regressor_plot(X_train,X_test,y_train,y_test,depth_list)

    
# Write your solution here :



