import pandas as pd

# Load the CSV file
file_path = 'opec_basket_price.csv'
data = pd.read_csv(file_path)

# Ensure the date column is in datetime format, with day-first format
data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)

# Set the date as the index
data.set_index('Date', inplace=True)

# Resample the data to daily, weekly, and monthly intervals
daily_data = data.resample('D').mean()  # Daily mean prices
weekly_data = data.resample('W').mean()  # Weekly mean prices
monthly_data = data.resample('M').mean()  # Monthly mean prices

# Save the resampled data to new CSV files
daily_data.to_csv('opec_basket_price_daily.csv')
weekly_data.to_csv('opec_basket_price_weekly.csv')
monthly_data.to_csv('opec_basket_price_monthly.csv')

print("Files created successfully: opec_basket_price_daily.csv, opec_basket_price_weekly.csv, opec_basket_price_monthly.csv")
