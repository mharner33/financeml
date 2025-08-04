import requests
import fmpsdk
from dotenv import load_dotenv
import os

load_dotenv()

fmp_api_key = os.getenv("FMP_API_KEY")
print(fmp_api_key)

def main():
    # Example: Get historical stock data for Apple
    try:
        historical_data = fmpsdk.historical_price_full(apikey=fmp_api_key, symbol='MP')
        print(historical_data[:5]) # Print the first 5 entries
    except Exception as e:
        print(f"An error occurred: {e}")
    


if __name__ == "__main__":
    main()
