import pandas as pd
import numpy as np

# Sample dataset
data = {'Date': ['2018-01-01', '2018-01-02']}
df = pd.DataFrame(data)

# Ordinal Encoding
df['Ordinal_Encoded'] = pd.to_datetime(df['Date']).astype(int)

# Extract Components
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

# Cyclical Encoding (for day of the week)
df['DayOfWeek_sin'] = np.sin(2 * np.pi * df['Date'].dt.dayofweek / 7)
df['DayOfWeek_cos'] = np.cos(2 * np.pi * df['Date'].dt.dayofweek / 7)

# Save to CSV
df.to_csv('encoded_dates.csv', index=False)

# Display the encoded DataFrame
print(df)
