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
    unit = ["USD","CAD","BTC","AUD","Yen","Eur"]
    if from_currency not in unit or to_currency not in unit:
        print("Invalid error")



    # inputs
    # required: amount of currency
    # optional: original currency type default CAD
    # optional: converted currency type default USD
    return round(converted, 4)
    # returns the number of what you are converting to along with units
    # round answers to 4 decimals


if __name__ == "__main__":
    assert convert(1.35) == 1   #1.35cad+1usd
    assert convert(1,"USD") == 1 #1usd=1usd
    assert convert(1,"USD","CAD") == 1.35 #1usd=1.35cad
    assert convert(1,"BTC") == 62000 #1btc=6200usd
    assert convert(1,"BTC","CAD") == 83700 #1btc=62000usd*1.35cad
    assert convert(1,"BTC","Eur") == 57943.93 #1btc=62000usd/1.07eur
    
    
