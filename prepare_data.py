import pandas as pd
import string

# Load the dataset
data = pd.read_csv('tasks.csv')

#preprocessing
data['Description'] = data['Description'].str.lower()
data['Description'] = data['Description'].str.translate(str.maketrans('', '', string.punctuation))
# Handling Missing Data
data.dropna(inplace=True)

data.to_csv('preprocessed_data.csv', index=False)