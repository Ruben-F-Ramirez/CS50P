import json
import requests
import sys


def main():
    
    call_price(com_check())

def call_price(val):
    try:
        r = requests.get('https://api.coincap.io/v2/assets/bitcoin')
        response = r.json()
        bitcoin = float(response["data"]["priceUsd"])
        amount = bitcoin * val
        print(f"${amount:,.4f}")
    except requests.RequestException:
        sys.exit("Request exception")

def com_check():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    
    try:
        return float(sys.argv[1])
    except:
        sys.exit("Command-line argument is not a number")

main()
