import pandas as pd
import numpy as np
import random

# Set random seed for reproducibility
np.random.seed(0)

# Generate data for 10 years (2012 to 2021)
years = list(range(2012, 2022))
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

            # Determine special occasion (1 for normal days, 2 for public events)
            if month == 1 and day == 1:  # New Year's Day
                special_occasion = 2
            elif month == 12 and day == 25:  # Christmas
                special_occasion = 2
            elif month == 7 and day == 4:  # Independence Day
                special_occasion = 2
            elif month == 10 and day == 31:  # Halloween
                special_occasion = 2
            elif month == 11 and day == 11:  # Veterans Day
                special_occasion = 2
            elif month == 5 and day == 1:  # Labor Day
                special_occasion = 2
            else:
                special_occasion = 1  # Normal day

            # Calculate quantity sold based on weather conditions and special occasions
            if temperature > 30 and precipitation < 5:
                quantity = np.random.randint(40, 60)  # Higher sales on hot and dry days
            elif temperature < 10:
                quantity = np.random.randint(5, 20)  # Fewer sales on cold days
            elif special_occasion == 2:
                quantity = np.random.randint(50, 70)  # Higher sales on special occasions
            else:
                quantity = np.random.randint(20, 40)  # Average sales on normal days

            # Append data to the list
            data.append([day, month, year, temperature, precipitation, special_occasion, quantity])

# Create DataFrame
columns = ['Day', 'Month', 'Year', 'Temperature', 'Precipitation', 'Special Occasion', 'Qty']
df = pd.DataFrame(data, columns=columns)

# Save DataFrame to CSV
df.to_csv('12to22.csv', index=False)
