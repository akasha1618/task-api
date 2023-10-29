import pandas as pd
import string

# Load the dataset
data = pd.read_csv('tasks_generated.csv')

#preprocessing
data['Description'] = data['Description'].str.lower()
#remove punctuation
data['Description'] = data['Description'].str.translate(str.maketrans('', '', string.punctuation))

# Removing empty lines from each entry so the email format will not have empty lines
data['Description'] = data['Description'].apply(lambda x: ' '.join(x.splitlines()))

# Handling Missing Data
data.dropna(inplace=True)

data.to_csv('preprocessed_data.csv', index=False)