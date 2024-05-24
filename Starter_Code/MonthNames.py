import pandas as pd

# Map month numbers to month names
month_names = {
    1: 'Sagittarius (Dec)',
    2: 'Dhanus (Jan)',
    3: 'Capricornus (Feb)',
    4: 'Aquarius (Mar)',
    5: 'Pisces (Apr)',
    6: 'Aries (May)',
    7: 'Taurus (Jun)',
    8: 'Gemini (Jul)',
    9: 'Cancer (Aug)',
    10: 'Leo (Sep)',
    11: 'Virgo (Oct)',
    12: 'Libra (Nov)'
}

# Create a DataFrame with month numbers and month names
month_df = pd.DataFrame(list(month_names.items()), columns=['month', 'month_name'])

# Print the DataFrame
print(month_df)

# Write the DataFrame to a CSV file
month_df.to_csv('D:\ASU_Bootcamp_Anaconda\Module 11 Challenge\Starter_Code\month_numbers_and_names.csv', index=False)
