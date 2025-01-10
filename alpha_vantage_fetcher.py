import os
from dotenv import load_dotenv
import requests
import pandas as pd

# Load the .env file
load_dotenv()

# Get the API key
api_key = os.getenv("ALPHA_VANTAGE_API_KEY")

if not api_key:
    print("Failed to load the API key. Please check your .env file.")
    exit()

print("Loaded API key")

# Input for stock symbol
stock_symbol = input("Enter the stock symbol (e.g., AAPL for Apple): ").upper()

# API Endpoint
base_url = "https://www.alphavantage.co/query"
params = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": stock_symbol,
    "interval": "5min",
    "apikey": api_key,
}

# Fetch stock data
response = requests.get(base_url, params=params)
data = response.json()

# Check for errors
if "Error Message" in data:
    print(f"Error in response: {data}")
    exit()
elif "Time Series (5min)" not in data:
    print("Unexpected response format. Please try again later.")
    exit()

# Extract time series data
time_series = data["Time Series (5min)"]

# Convert to a DataFrame for better readability
df = pd.DataFrame.from_dict(time_series, orient="index")
df.columns = ["Open", "High", "Low", "Close", "Volume"]
df.index.name = "Timestamp"

# Display the first 10 rows
print("\nLatest Stock Data (Top 10 entries):")
print(df.head(10))

# Save to a CSV file
csv_filename = f"{stock_symbol}_stock_data.csv"
df.to_csv(csv_filename)
print(f"\nData saved to {csv_filename}")
