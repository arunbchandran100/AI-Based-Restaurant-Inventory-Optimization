import pandas as pd

# Read your CSV file
df = pd.read_csv('final_mandi_dataset_date.csv')

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Extract Year, Month, and Day
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

# Display or save the modified DataFrame
print(df)

# Save to a new CSV file
df.to_csv('date_format_final_mandi.csv', index=False)
