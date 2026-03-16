import pandas as pd

# Load the dataset
data = pd.read_csv("../source/assessment_1_database_csvfile.csv")

# Show data
print(data.head())
print(data.info())
print(data.describe())