def calc_dollars():
    piggy_bank = {
        "quarters": 45,
        "nickels": 53,
        "dimes": 62,
        "pennies": 71,
    }

    dollar_amount = 0

    for coin, amount in piggy_bank.items():
        if (coin == "quarters"):
            dollar_amount += (amount * .25)
        elif (coin == "nickels"):
            dollar_amount += (amount * .05)
        elif (coin == "dimes"):
            dollar_amount += (amount * .10)
        elif (coin == "pennies"):
            dollar_amount += (amount * .01)

    return 	"{:.2f}".format(dollar_amount)

print("$", calc_dollars())