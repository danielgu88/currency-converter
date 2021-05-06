rates = {"RUB": 2.98, "ARS": 0.82, "HNL": 0.17, "AUD": 1.9622, "MAD": 0.208}

conicoins = float(input())

for key, value in rates.items():
    print("I will get {} {} from the sale of {} conicoins."
          .format(round(conicoins * value, 2), key, float(conicoins)))
