# Data Preprocessing Template

# Importing the dataset
dataset = read.csv('Data.csv')

# Taking care of missing data
dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Age)


dataset$Salary = ifelse(is.na(dataset$Salary),
                        ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
                        dataset$Salary)

dataset$Country = factor(dataset$Country,
                         levels = c('France', 'Spain', 'Germany'),
                         labels = c(1, 2, 3))

dataset$Purchased = factor(dataset$Purchased,
                           levels = c('Yes', 'No'),
                           labels = c(1, 0))

# Splitting the dataset into the Training set and Test set
# you need to install library, so for the first time run this:
#install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature Scaling
# factor columns should be expluced since they are nit numeric despite their appearance
training_set[, 2:3] = scale(training_set[, 2:3])
test_set[, 2:3] = scale(test_set[, 2:3])

#problem here: we have different scale for train and test (since they are scaled independently)
# to have identical scale:
# train_center <- colMeans(X_training[,1:2],  na.rm=T)
# train_scale <- sapply(X_training[,1:2], FUN=function(col) sd(col, na.rm=T))
# X_train[,1:2] <- scale(X_train[,1:2])
# X_test[,1:2] <- scale(X_test[,1:2], center=train_center, scale=train_scale)