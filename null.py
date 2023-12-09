import pandas as pd
import numpy as np

# Load the data
df = pd.read_csv("./diamonds.csv")

# Define the probability of creating null values
null_probability = 0.05  # Adjust this value as needed

# Create random null values in the 'carat' and 'price' columns
df['carat'] = np.where(np.random.random(len(df)) < null_probability, np.nan, df['carat'])
df['price'] = np.where(np.random.random(len(df)) < null_probability, np.nan, df['price'])

# Save the data with random null values
df.to_csv("diamonds_with_null.csv", index=False)