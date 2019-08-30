def add_money(balance, amount):
    """Add money to a bank account

    Arguments:
      amount - A numerical value by which the bank account's balance will increase
    """
    try:
      balance += amount
      print(f"{balance}")
    except TypeError:
      print('(Error): The add_money method requies a numeric value')
      raise

add_money(0, 10)