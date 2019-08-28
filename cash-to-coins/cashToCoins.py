dollarAmount = 8.69

piggyBank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}

# Your magic Python code here
def calc_coins(dolors):
    remainder_quarters = float("{0:.2}".format(dolors % .25))
    piggyBank["quarters"] = round((dolors - remainder_quarters) / .25)
    remainder_dimes = float("{0:.2}".format(remainder_quarters % .10))
    piggyBank["dimes"] = round((remainder_quarters - remainder_dimes) / .10)
    remainder_nickels = float("{0:.2}".format(remainder_dimes % .05))
    piggyBank["nickels"] = round((remainder_dimes - remainder_nickels) / .05)
    remainder_pennies = float("{0:.2}".format(remainder_nickels % .01))
    piggyBank["pennies"] = round((remainder_nickels - remainder_pennies) / .01)

calc_coins(dollarAmount)