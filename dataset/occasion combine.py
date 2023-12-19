import pandas as pd

# Load synthetic dataset
synthetic_df = pd.read_csv("base_mandi_dataset.csv")

# Load special occasion dataset
special_occasion_df = pd.read_csv("int_special_occasion.csv")

# Convert 'Date' column to datetime type
synthetic_df['Date'] = pd.to_datetime(synthetic_df['Date'])
special_occasion_df['Date'] = pd.to_datetime(special_occasion_df['Date'])

# Drop duplicate special occasions for the same date
special_occasion_df = special_occasion_df.drop_duplicates(subset=['Date'])

# Merge the datasets
merged_df = pd.merge(synthetic_df, special_occasion_df, how="left", on="Date")

# Create a new column 'Special Occasion' and fill it with 'Normal Day'
merged_df['Special Occasion'] = 'Normal Day'

# Replace NaN values in 'Special Occasion' with the actual special occasion
merged_df.loc[~merged_df['special occasion'].isna(), 'Special Occasion'] = merged_df['special occasion']

# Drop the redundant 'special occasion' column
merged_df = merged_df.drop(columns=['special occasion'])

# Save the merged DataFrame to a new CSV file
merged_df.to_csv("S_o_mandi_dataset.csv", index=False)
