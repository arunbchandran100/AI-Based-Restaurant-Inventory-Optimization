import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

# Read the CSV file
df = pd.read_csv('Final_merged_dataset.csv')

# Remove leading and trailing whitespaces in column names
df.columns = df.columns.str.strip()

# Convert categorical columns to numerical using Label Encoding
label_encoder = LabelEncoder()

# Assuming 'Special Occasion' is the correct column name
df['Special_Occasion'] = label_encoder.fit_transform(df['Special Occasion'])

# One-hot encode the 'Food item' column
onehot_encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')
df_food_encoded = pd.DataFrame(onehot_encoder.fit_transform(df[['Food item']]))
df = pd.concat([df, df_food_encoded], axis=1)

# Drop the original 'Food item' column
df = df.drop(['Food item'], axis=1)

# Separate features (X) and target variable (y)
X = df.drop(['Qty', 'Date'], axis=1)
y = df['Qty']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest Regressor
rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)

# Fit the model on the training data
rf_regressor.fit(X_train, y_train)

# Make predictions on the test data
predictions = rf_regressor.predict(X_test)

# Evaluate the model performance
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error on the test set: {mse}")
