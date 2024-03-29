import pandas as pd
import numpy as np
import random

# Set random seed for reproducibility
np.random.seed(0)

# Generate data for 10 years (2012 to 2021)
years = list(range(1950, 2022))
months = list(range(1, 13))
days = list(range(1, 32))

data = []

for year in years:
    for month in months:
        for day in days:
            # Generate temperature (normally distributed with mean 25 and std dev 5)
            temperature = np.random.normal(25, 5)

            # Generate precipitation (normally distributed with mean 10 and std dev 5)
            precipitation = np.random.normal(10, 5)

            # Generate special occasion (1 for normal days, 2 for special occasions)
            special_occasion = np.random.choice([1, 2], p=[0.9, 0.1])

            # Calculate quantity sold based on weather conditions and special occasions
            if precipitation > 15:
                quantity = np.random.randint(5, 20)  # Fewer sales on rainy days
            elif special_occasion == 2:
                quantity = np.random.randint(40, 60)  # Higher sales on special occasions
            else:
                quantity = np.random.randint(20, 40)  # Average sales on normal days

            # Append data to the list
            data.append([day, month, year, temperature, precipitation, special_occasion, quantity])

# Create DataFrame
columns = ['Day', 'Month', 'Year', 'Temperature', 'Precipitation', 'Special Occasion', 'Qty']
df = pd.DataFrame(data, columns=columns)

# Save DataFrame to CSV
df.to_csv('dataset_updated.csv', index=False)
