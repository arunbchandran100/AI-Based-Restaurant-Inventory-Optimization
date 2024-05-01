import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Load the dataset
# Make sure to upload the '12to22.csv' file in your environment
dataset = pd.read_csv('12to22.csv')

# Split the dataset into features (X) and target variable (y)
X = dataset.drop(columns=['Qty'])  # Features
y = dataset['Qty']  # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=60)

# Initialize the Random Forest Regressor
rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model
rf_regressor.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rf_regressor.predict(X_test)



# Example new data input including Day, Month, and Year
new_data = pd.DataFrame({
    'Day': [24],  # Example Day
    'Month': [7],  # Example Month
    'Year': [2022],  # Example Year
    'Temperature': [35], 
    'Precipitation': [10], 
    'Special Occasion': [1]
}, index=[0])

predicted_quantity = rf_regressor.predict(new_data)
print("Predicted Quantity:", predicted_quantity[0])