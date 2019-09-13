def laundry():
    return "The dirty laundry was cleaned"

def garbage():
    return "The garbage was taken out"

def dust():
    return "The house was dusted"

def groom():
    return "The dog was brushed"

def kids(func):
    def by_kids():
        return f"{func()} by the kids"

    return by_kids

def mom(func):
    def by_mom():
        return f"{func()} by the mom"

    return by_mom

def dad(func):
    def by_dad():
        return f"{func()} by the dad"

    return by_dad

@kids
def garbage():
    return "The garbage was taken out"

@mom
def garbage():
    return "The garbage was taken out"

# @dad
# def garbage():
#     return "The garbage was taken out"

result = garbage()
print(result)  # "The garbage was taken out by the kids"