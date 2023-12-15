# Import libraries
import pandas as pd
from faker import Faker
import random

# Create a Faker object
fake = Faker()

# Define the food items
food_items = ["ADD FRIES", "ADD HAZELNUT FLAVOUR", "ADD TRADITIONAL MEAT FEAST", "AL SIKANDARI HOOKAH SINGL", "B1G1 ZINZI WHITE (BTL)", "BRAZIL BOURBONSANTOS (AULAIT)", "BUN MASKA & CHAI", "BUTTER MILK PAN CAKES", "CARLSBERG", "CARROT CAKE", "CREPES WITH MUSHROOMS", "CRUMBED TOFU CRUSTINI", "CURRANT COOLER", "DOPPIO", "DUTCH TRUFFLE CAKE SHAKE", "ESPRESSO", "GARDEN FRESH PANINI", "GREAT LAKES SHAKE", "HOUSE BLEND DECAFF (REG)", "HOUSEBLEND FULLCITY (REG)", "ICED LEMON OR STR CAMOMILE", "ITALIAN CAPONATA PANINO", "ITALIAN OMELETTE BREAKFAST", "JAPANESE YAKITORI WRAP", "JR.CHL AVALANCHE", "JUICE HOOKAH SINGLE", "KENYA AA (AULAIT)", "MONSOON MALABAR (REG)", "NON-VEG CLUB WRAP", "NUTELLA CREPES", "ORANGE ARRABIATA", "ORANGINA  (250ML)", "OREO COOKIE SHAKE", "PESCADO PANINO", "PINK LEMONADE", "PLAIN JANE (CHOCOLATE)", "QUA  MINERAL WATER(500ML)", "RED SANGRIA (CARAFE)", "RED WINE SHEESHA", "SAMBUCA", "SANGRIA ROSE (CARAFE)", "SATAY CHICKEN PANINI", "SCRAMBLED EGGS", "SPANISH OMELETTE BREAKFAST", "SR.CHL AVALANCHE", "THE CHOCO LATTE", "TIRAMISU", "TOBLERONE SHAKE", "ULTIMATE HOT CHOCOLATE", "VANILLA ICECREAM"]

# Define the number of rows
n_rows = 365 * 6 # 6 years from 2010 to 2015

# Create empty lists for each column
dates = []
foods = []
qtys = []
temps = []
precs = []

# Generate fake data for each column
for i in range(n_rows):
    # Generate a random date between 2010-01-01 and 2015-12-31
    date = fake.date_between(start_date="-6y", end_date="today")
    dates.append(date)

    # Generate a random food item from the list
    food = random.choice(food_items)
    foods.append(food)

    # Generate a random quantity between 1 and 52
    qty = random.randint(1, 52)
    qtys.append(qty)

    # Generate a random temperature between 15 and 35
    temp = random.randint(15, 35)
    temps.append(temp)

    # Generate a random precipitation between 0.8 and 32.8
    prec = round(random.uniform(0.8, 32.8), 1)
    precs.append(prec)

# Create a pandas DataFrame from the lists
df = pd.DataFrame({"Date": dates, "Food item": foods, "Qty": qtys, "Temperature": temps, "Precipitation": precs})

# Sort the DataFrame by date
df = df.sort_values(by="Date")

# Reset the index
df = df.reset_index(drop=True)

# Save the dataset to a csv file
df.to_csv("2synthetic_data.csv", index=False)

# Print the first 5 rows
print(df.head())
