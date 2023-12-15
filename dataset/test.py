import csv
import random
from datetime import datetime, timedelta

# Function to generate random data for a given year
def generate_data_for_year(year, event_probabilities):
    data = []
    start_date = datetime(year, 1, 1)
    end_date = datetime(year, 12, 31)

    while start_date <= end_date:
        week_number = start_date.isocalendar()[1]
        food_items = {f"Food_Item_{i}": random.randint(20, 80) for i in range(1, 6)}
        event = random.choices(["None", "Seasonal", "Special_Event", "Valentine's_Day", "Christmas"], event_probabilities)[0]
        inventory_status = random.choices(["Underflow", "Correct", "Overflow"], [0.1, 0.7, 0.2])[0]

        row = [start_date.strftime("%Y-%m-%d"), week_number] + [f"{item}:{quantity}" for item, quantity in food_items.items()] + [event, inventory_status]
        data.append(row)

        start_date += timedelta(days=1)

    return data

# Set random seed for reproducibility
random.seed(42)

# Define event probabilities for each year
event_probabilities = {
    2013: [0.6, 0.1, 0.1, 0.1, 0.1],
    2014: [0.5, 0.1, 0.2, 0.1, 0.1],
    2015: [0.6, 0.1, 0.1, 0.1, 0.1],
    2016: [0.5, 0.1, 0.2, 0.1, 0.1],
    2017: [0.6, 0.1, 0.1, 0.1, 0.1],
    2018: [0.5, 0.1, 0.2, 0.1, 0.1],
    2019: [0.6, 0.1, 0.1, 0.1, 0.1],
    2020: [0.5, 0.1, 0.2, 0.1, 0.1],
    2021: [0.6, 0.1, 0.1, 0.1, 0.1],
    2022: [0.5, 0.1, 0.2, 0.1, 0.1],
}

# Create a CSV file with data for the previous 10 years
with open("restaurant_data.csv", "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Date", "Week", "Food_Item_1", "Food_Item_2", "Food_Item_3", "Food_Item_4", "Food_Item_5", "Event", "Inventory_Status"])

    for year in range(2013, 2023):
        year_data = generate_data_for_year(year, event_probabilities[year])
        csv_writer.writerows(year_data)

print("CSV file 'restaurant_data.csv' has been generated.")
