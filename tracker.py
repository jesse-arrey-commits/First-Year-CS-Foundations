import sys
import requests

def fetch_exchange_rate(base_currency: str, target_currency: str) -> None:
    # clean the incoming text arguments
    base_currency = base_currency.lower().strip()
    target_currency = target_currency.lower().strip()
    
    # build the url using the cleaned base currency
    url = f"https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{base_currency}.json"

    # request data across network and parse the returning text into a dictionary
    response = requests.get(url)
    data = response.json()

    # extract the nested price number
    rate = data[base_currency][target_currency]
    print(f"📈 1 {base_currency.upper()} = {rate:,.2f} {target_currency.upper()}")

    # personal boundary alert for home currency
    if base_currency == 'cad' and target_currency == 'xaf':
        if rate >= 415.0:
            print("🚀 Alert: Excellent exchange rate! Ideal time to send money home.")
        else:
            print("⏳ Notice: Baseline rate. You may want to wait for a stronger peak.")
    
    # permanent file I/O logging
    with open("history.txt", "a") as file:
        file.write(f"1 {base_currency.upper()} = {rate:.2f} {target_currency.upper()}\n")

if __name__ == "__main__":

    # check if the user typed enough extra word after 'python.exe tracker.py'
    if len(sys.argv) > 2:
        source_currency = sys.argv[1]
        destination_currency = sys.argv[2]
        
        # call the function and pass both inputs into it 
        fetch_exchange_rate(source_currency, destination_currency)
    else: 
        print("❌ Usage Error! Example: python tracker.py cad xaf")
