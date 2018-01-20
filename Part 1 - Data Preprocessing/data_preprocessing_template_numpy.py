# Data Preprocessing Template
# Using numpy methods here to fill N/A values and implement One-Hot encoding
# See corresponding file for same operations using Pandas
# comparing Numpy vs Pandas in terms of performance: http://gouthamanbalaraman.com/blog/numpy-vs-pandas-comparison.html

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

# imputation - means replacing n/a values with some meaninful approximation, here we use mean of existing values
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:, 1:3])    #fit = calculate value based on data in parameter
X[:, 1:3] = imputer.transform(X[:, 1:3]) # perform the actual replacement

# LabelEncoder - replace values with int numbers (enumerate them)
# problem with LabelEncoder - int numbers have order built into them, which might be unwanted side effect
# OneHotEncoder solves the problem by using separate column for each value with values 0 or 1
# names comes from the fact that for each row only one column will have 1 and others will have 0
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0]) #fit and transform in one method

onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()    #we need toarray() to convert from sparse matrix

y = LabelEncoder().fit_transform(y)

X2 = pd.DataFrame(X)   #if array has dtype=object, you can't explore it in Variable explorer, this conversion helps


# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)