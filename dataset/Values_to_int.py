import pandas as pd

# Read the CSV file
df = pd.read_csv('merged_dataset.csv')

# Define mapping dictionaries
day_mapping = {'Sunday': 1, 'Monday': 2, 'Tuesday': 3, 'Wednesday': 4, 'Thursday': 5, 'Friday': 6, 'Saturday': 7}
month_mapping = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
                 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}

# Apply mappings to 'Day' and 'Month' columns
df['Day'] = df['Day'].map(day_mapping)
df['Month'] = df['Month'].map(month_mapping)

# Define special occasion categories
general_events = ['New Year\'s Day (R)', 'Christmas Eve (R)', 'Christmas Day (G)', 'Independence day (G)',
                  'Mahatma Gandhi\'s Birthday (G)', 'Onam or Thiru Onam Day (R)', 'Raksha Bandhan (R)',
                  'Rath Yatra (R)', 'Republic Day (G)', 'Maha Shivaratri (G)', 'Mahavir Jayanti (G)']

hindu_events = ['Makar Sankranti (R)', 'Basant Panchami / Sri Panchami (R)', 'Guru Ravidas\'s Birthday (R)',
                'Swami Dayananda Saraswati Jayanti (R)', 'Holika Dahan/Dolyatra (R)', 'Holi (G)',
                'Chaitra Sukladi/Gudi Padava/Ugadi/Cheti Chand (R)', 'Ram Navami (R)', 'Shivaji Jayanti (R)',
                'Vaisakhi/Vishu/Mesadi (R)', 'Vaisakhadi(Bengal)/Bahag Bihu (Assam) (R)', 'Buddha Purnima (G)',
                'Guru Rabindranath\'s Birthday (R)', 'Dussehra (Maha Saptami) (Additional) (R)',
                'Dussehra (Maha Ashtami) (Additional) (R)', 'Dussehra (Maha Navmi) (R)', 'Dussehra (G)',
                'Maharishi Valmiki\'s Birthday (R)', 'Karaka Chaturthi (Karva Chouth) (R)', 'Deepavali (South India) (R)',
                'Diwali (Deepavali) (G)', 'Gur\'u Nanak\'s Birthday (G)', 'Guru Teg Bahadur\'s Martyrdom Day (R)',
                'Govardhan Puja (R)', 'Bhai Duj (R)', 'Pratihar Sashthi or Surya Sashthi (Chhat Puja) (R)',
                'Janmashtami (G)', 'Vinayaka Chaturthi/Ganesh Chaturthi (R)']

christian_events = ['Easter Sunday (R)', 'Good Friday (G)']

muslim_events = ['Jamat-Ul-Vida (R)', 'Idu\'l Fitr (G)', 'Milad-un-Nabi or Id-e-Milad (Birthday of Prophet Mohammad) (G)',
                 'Muharram (G)', 'Parsi New Year\'s day/Nauraj (R)', 'Id-ul-Zuha (Bakrid) (G)']

# Create a new column 'Special Occasion Category' and classify each special occasion
df['Special Occasion Category'] = 1  # Default to 'Normal Day'

# Classify general events
df.loc[df['Special Occasion'].isin(general_events), 'Special Occasion Category'] = 2

# Classify Hindu events
df.loc[df['Special Occasion'].isin(hindu_events), 'Special Occasion Category'] = 3

# Classify Muslim events
df.loc[df['Special Occasion'].isin(muslim_events), 'Special Occasion Category'] = 4

# Classify Christian events
df.loc[df['Special Occasion'].isin(christian_events), 'Special Occasion Category'] = 5

# Save the modified DataFrame to a new CSV file
df.to_csv('int_values_merged_dataset.csv', index=False)

print("Conversion completed. Check 'output.csv'")
