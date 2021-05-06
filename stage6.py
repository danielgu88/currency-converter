import requests

cache = {}
currency_code = input().lower()

response = requests.get("http://www.floatrates.com/daily/{}.json".format(currency_code))
dictionary = eval(response.text)

if currency_code != "usd":
    cache["usd"] = dictionary["usd"]["rate"]

if currency_code != "eur":
    cache["eur"] = dictionary["eur"]["rate"]

currency_code_receive = input().lower()

while currency_code_receive != "":
    amount = float(input())
    print("Checking the cache...")

    if currency_code_receive in cache:
        print("Oh! It is in the cache!")
    else:
        print("Sorry, but it is not in the cache!")
        cache[currency_code_receive] = dictionary[currency_code_receive]["rate"]

    print("You received {} {}."
          .format(round(amount * cache[currency_code_receive], 2), currency_code_receive.upper()))

    currency_code_receive = input().lower()
