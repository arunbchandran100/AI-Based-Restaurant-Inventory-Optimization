import pandas as pd
from datetime import datetime, timedelta
from sklearn.ensemble import RandomForestRegressor
import numpy as np

# Load the dataset
dataset_path = "mandi_merged_dataset.csv"
df = pd.read_csv(dataset_path)

# Convert categorical variables to numerical
df = pd.get_dummies(df, columns=["Day", "Month", "Special Occasion"])

# Split the dataset into features (X) and target variable (y)
X = df.drop(["Date", "Food item", "Qty"], axis=1)
y = df["Qty"]

# Initialize the Random Forest Regressor
rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)

# Fit the model
rf_regressor.fit(X, y)

# Now, let's predict the sales data for the year 2024
# Generate dates for the year 2024
start_date_2024 = pd.to_datetime("2024-01-01")
end_date_2024 = pd.to_datetime("2024-12-31")
date_range_2024 = pd.date_range(start=start_date_2024, end=end_date_2024, freq="D")

# Create a DataFrame with the features for the year 2024
features_2024 = pd.DataFrame({"Date": date_range_2024})

# Extract day, month, and special occasion information from the date
features_2024["Day"] = features_2024["Date"].dt.day_name()
features_2024["Month"] = features_2024["Date"].dt.month_name()
features_2024["Special Occasion"] = "Normal Day"  # Assuming it's a normal day by default

# Convert categorical variables to numerical
features_2024 = pd.get_dummies(features_2024, columns=["Day", "Month", "Special Occasion"])

# Ensure feature names match between training and test sets
missing_features = set(X.columns) - set(features_2024.columns)
for feature in missing_features:
    features_2024[feature] = 0

# Make predictions for the year 2024
predictions_2024 = rf_regressor.predict(features_2024.drop("Date", axis=1))

# Create a DataFrame with the predicted quantities and corresponding dates
predicted_df = pd.DataFrame({"Date": date_range_2024, "Predicted Qty": predictions_2024})

# Save the predicted data to a CSV file
predicted_df.to_csv("predicted_mandi.csv", index=False)
