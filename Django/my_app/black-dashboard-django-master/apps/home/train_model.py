import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load the dataset
dataset = pd.read_csv('12to22.csv')

# Split the dataset into features (X) and target variable (y)
X = dataset.drop(columns=['Qty'])
y = dataset['Qty']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=60)

# Initialize and train the Random Forest Regressor
rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)
rf_regressor.fit(X_train, y_train)

# Save the trained model to a file
joblib.dump(rf_regressor, 'rf_regressor.pkl')
