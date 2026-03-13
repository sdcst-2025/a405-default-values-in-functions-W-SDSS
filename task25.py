#!python3
# Currency Conversion
"""
Most of the time, in Canada, we convert our money
into USD. But we could also travel to other places

Create a function that accepts:
required: 1 positional argument - amount of money to convert
optional:
1 argument: currency to convert from default CAD
1 argument: currency to covnert to default USD

Conversion rates to use:
1 USD = 1.35 CAD
1 BTC = 62000 USD
1 USD = 1.51 AUD
1 USD = 155 Yen
1 Eur = 1.07 USD

Units must be in ["USD","CAD","BTC","AUD","Yen","Eur"]
"""
def convert(amount, from_currency="CAD", to_currency="USD"):
    
    if from_currency == "USD":
       usd = amount
    elif from_currency == "CAD":
       usd = amount/1.35
    elif from_currency == "BTC":
       usd = amount*62000
    elif from_currency == "AUD":
       usd = amount/1.51
    elif from_currency == "Yen":
       usd = amount/155
    elif from_currency == "Eur":
       usd = amount*1.07

    if to_currency == "USD":
       converted = usd
    elif to_currency == "CAD":
       converted = usd*1.35
    elif to_currency  == "BTC":
       converted = usd/62000
    elif to_currency == "AUD":
       converted = usd*1.51
    elif to_currency == "Yen":
       converted = usd*155
    elif to_currency == "Eur":
       converted = usd/1.07

    return round(converted, 4)

if __name__ == "__main__":
   assert convert(1.35) == 1
   assert convert(1,"USD") == 1
   assert convert(1,"USD","CAD") == 1.35
   assert convert(1,"BTC") == 62000
   assert convert(1,"BTC","CAD") == 83700
   assert convert(1,"BTC","Eur") == 57943.93

    # inputs
    # required: amount of currency
    # optional: original currency type default CAD
    # optional: converted currency type default USD
    # returns the number of what you are converting to along with units
    # round answers to 4 decimals
