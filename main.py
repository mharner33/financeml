import requests
from fmpsdk import quote
def main():
    print("Hello from financeml!")
    quote.quote("AAPL")
    

if __name__ == "__main__":
    main()
