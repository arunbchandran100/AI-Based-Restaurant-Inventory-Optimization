import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Define the start and end dates for the dataset
start_date = datetime(2018, 1, 1)
end_date = datetime(2023, 12, 31)

# Generate a date range for the specified period
date_range = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]

# Define food items
food_items = ["1","2","3"]

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic data
data = []
for date in date_range:
    for food_item in food_items:
        temperature = np.random.randint(15, 30)
        precipitation = np.round(np.random.uniform(0.8, 32.8), 1)
        qty = np.random.randint(1, 53)  # Qty range (1 to 52)

        # Extract day and month from the date
        day_name = date.strftime("%A")  # Day name (Monday, Tuesday, etc.)
        month_name = date.strftime("%B")  # Month name (January, February, etc.)

        # Define special occasions based on date
        special_occasion = "Normal Day"
        if date.month == 1 and date.day == 1:
            special_occasion = "New Year"
        # Add more conditions for other special occasions

        data.append([date, food_item, qty, temperature, precipitation, day_name, month_name, special_occasion])

# Create DataFrame
columns = ["Date", "Food item", "Qty", "Temperature", "Precipitation", "Day", "Month", "Special Occasion"]
df = pd.DataFrame(data, columns=columns)

# Save DataFrame to CSV
df.to_csv("3_items_dataset.csv", index=False)
