## Importing necessary libraries:
import pandas as pd

##Loading the dataset:
# Assuming the dataset is in a CSV file format
dataset = pd.read_csv('dataset.csv')

## Checking the dimensions of the dataset:
print("Number of rows:", dataset.shape[0])
print("Number of columns:", dataset.shape[1])

## Displaying the first few rows of the dataset:
print(dataset.head())
Analyzing Descriptive Statistics:

## Calculating summary statistics:
# Summary statistics for numerical columns
print(dataset.describe())
# Summary statistics for categorical columns
print(dataset.describe(include='object'))

## Computing column-wise statistics:
# Mean of a numerical column
print(dataset['column_name'].mean())
# Mode of a categorical column
print(dataset['column_name'].mode())

## Visualizing Data Distributions:
## Importing visualization libraries:
import matplotlib.pyplot as plt
import seaborn as sns

## Creating histograms:
# Histogram of a numerical column
sns.histplot(data=dataset, x='column_name')
plt.show()

## Generating bar plots:
# Bar plot of a categorical column
sns.countplot(data=dataset, x='column_name')
plt.show()

## Plotting boxplots:

# Box plot of a numerical column
sns.boxplot(data=dataset, y='column_name')
plt.show()

## Identifying Missing Values and Outliers:
## Checking for missing values:
# Total missing values in each column
print(dataset.isnull().sum())
# Percentage of missing values in each column
print(dataset.isnull().sum() / len(dataset) * 100)

## Handling missing values:
# Dropping rows with missing values
dataset.dropna(inplace=True)
# Filling missing values with mean
dataset['column_name'].fillna(dataset['column_name'].mean(), inplace=True)

## Detecting outliers:
# Box plot to visualize outliers
sns.boxplot(data=dataset, y='column_name')
plt.show()

## Dealing with outliers:
# Removing outliers based on z-score
from scipy.stats import zscore
dataset = dataset[(np.abs(zscore(dataset['column_name'])) < 3)]

