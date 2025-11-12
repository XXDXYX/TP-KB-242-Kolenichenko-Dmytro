import requests

response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
def rates():
    for elem in response.json():
        if (elem["cc"] == "EUR" or elem["cc"] == "USD" or elem["cc"] == "PLN"):
            print(f"{elem['cc']} : {elem['rate']}")

rates()

def input_currency():
    currency = input("Enter currency code (EUR, USD, PLN): ").upper()
    return currency

def input_amount():
    amount = float(input("Enter amount of currency: "))
    return amount

def main():
    currency = input_currency()
    amount = input_amount()
    for elem in response.json():
        if elem["cc"] == currency:
            converted_amount = amount * elem["rate"]
            print(f"{amount} {currency} is equal to {converted_amount:.2f} UAH")
main()            