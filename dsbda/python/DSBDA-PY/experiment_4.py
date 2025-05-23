# -*- coding: utf-8 -*-
"""Experiment_4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pyrwIcMFYLR7okg_7-NMhOaRvpZxZF3h
"""

import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split

from sklearn.datasets import load_boston
boston = load_boston()
print(boston)

boston.feature_names

boston.target

x = pd.DataFrame(boston.data, columns = boston.feature_names)
y = pd.DataFrame(boston.target)

x.head(10)

y.head(10)

reg = linear_model.LinearRegression()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)

reg.fit(x_train, y_train)

print(reg.coef_)

y_pred = reg.predict(x_test)
print(y_pred)

