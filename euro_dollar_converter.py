import requests

# def get_eur_to_usd_rate(api_key):
#     url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/EUR"
#     response = requests.get(url)
#     if response.ok :
#         data = response.json()
#         if "USD" in data["conversion_rates"] :
#             return data["conversion_rates"]["USD"]
#         else :
#             print("Fout: USD wisselkoers niet gevonden.")
#             return None
#
#     else :
#         print(f"Fout: {response.status_code} - {response.text}")
#         return None
#
# def convert_eur_to_usd(amount, exchange_rate) :
#     return amount * exchange_rate
#
# def main() :
#     api_key = "4f43c80d4c687621e723dfc1"
#     eur_amount = float(input("Voer het bedrag in EUR in: ").strip())
#     exchange_rate = get_eur_to_usd_rate("4f43c80d4c687621e723dfc1")
#     if exchange_rate is not None :
#         usd_amount = convert_eur_to_usd(eur_amount, exchange_rate)
#         print(f"{eur_amount:.2f} EUR is gelijk aan {usd_amount:.2f} USD (Wisselkoers: 1 EUR = {exchange_rate} USD)")
#     else:
#         print("Kan geen wisselkoers ophalen.")
#
# if __name__ == "__main__" :
#     main()

#Bonus

def get_exchange_rate(api_key, from_currency, to_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"
    response = requests.get(url)
    if response.ok:
        data =  response.json()
        if to_currency in data["conversion_rates"]:
            return data["conversion_rates"][to_currency]
        else:
            print(f"Fout: {to_currency} wisselkoers niet gevonden.")
            return None
    else:
        print(f"Fout: {response.status_code} - {response.text}")

def main():
    api_key = "4f43c80d4c687621e723dfc1"
    from_currency = input("Van welke valuta? (bijvoorbeeld EUR): ").strip().upper()
    to_currency = input("Naar welke valuta? (bijvoorbeeld USD): ").strip().upper()
    amount = float(input(f"Voer het bedrag in {from_currency} in: ").strip())
    exchange_rate = get_exchange_rate(api_key, from_currency, to_currency)
    if exchange_rate is not None:
        converted = amount * exchange_rate
        print(f"{amount} {from_currency} is gelijk aan {converted:.2f} {to_currency} (Wisselkoers: 1"
              f" {from_currency} = {exchange_rate} {to_currency})")

if __name__ == "__main__":
    main()

