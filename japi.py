import sys,json
import requests

BASE_URL = "https://www.alphavantage.co/query"
def getStockData(symbol):
    params = {"function": "TIME_SERIES_DAILY", "symbol": symbol, "apikey":"WH97KT984QA66HBT", "outputsize":"compact" }
    response = requests.get(BASE_URL, params)
    return response.json()

def main():
    outFile = open('japi.out', 'w')
    while 1:
        userInput = input("Enter Stock Symbol or EXIT to exit: ").upper()
        if userInput != "EXIT":
            serverData = 'The current price of {} is {}\n'.format(userInput, getStockData(userInput))
            print(serverData)
            print("Stock Quotes retrieved successfully!")
            outFile.write(serverData)
        else:
            sys.exit("\nThank you for using the program!\n")

if __name__ == "__main__":
    main()