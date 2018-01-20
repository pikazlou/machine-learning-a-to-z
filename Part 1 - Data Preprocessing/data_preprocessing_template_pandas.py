# Data Preprocessing Template
# Using pandas methods here to fill N/A values and implement One-Hot encoding
# See corresponding file for same operations using Numpy
# comparing Numpy vs Pandas in terms of performance: http://gouthamanbalaraman.com/blog/numpy-vs-pandas-comparison.html

# Importing the libraries
#import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')

# imputation - means replacing n/a values with some meaninful approximation, here we use mean of existing values
dataset = dataset.fillna(dataset.mean())

# one hot encoding
country_dummy_df = pd.get_dummies(dataset['Country'])


combined_df = pd.concat(
        [dataset[['Age', 'Salary']],
         country_dummy_df],
         axis=1,
         join='inner')

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""