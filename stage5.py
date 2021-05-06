import requests

currency_code = input().lower()
response = requests.get("http://www.floatrates.com/daily/{}.json".format(currency_code))
dictionary = eval(response.text)

print(dictionary["usd"])
print(dictionary["eur"])
