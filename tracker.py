import sys
import requests

def fetch_exchange_rate(base_currency: str, target_currency: str) -> None:
    # 1. Standardise the word to Lowercase so the API can read it
    base_currency = base_currency.lower().strip()
    target_currency = target_currency.lower().strip()
    
    # 2. Build the target URL address string
    url = f"https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{base_currency}.json"

    # 3. Ping the network server and parse the returning text into a dictionary
    response = requests.get(url)
    data = response.json()

    rate = data[base_currency][target_currency]
    print(f"📈 1 {base_currency.upper()} = {rate:,.2f} {target_currency.upper()}")

    if base_currency == 'cad' and target_currency == 'xaf':
        if rate >= 415.0:
            print("🚀 Alert: Excellent exchange rate! Ideal time to send money home.")
        else:
            print("⏳ Notice: Baseline rate. You may want to wait for a stronger peak.")

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
        print("You didn't give me enough arguments! Launching default mode.")
    