running_kids = ["Pam", "Sam", "Andrea", "Will"]
swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]

def run(kid):
    print(f"{kid} ran")

def swing(kid):
    print(f"{kid} swung")

def slide(kid):
    print(f"{kid} slid")

def hide(kid):
    print(f"{kid} hid")

# for kid in running_kids:
#     run(kid)

# for kid in swinging_kids:
#     swing(kid)

# for kid in sliding_kids:
#     slide(kid)

# for kid in hiding_kids:
#     hide(kid)

for i in range(1, 101):
    if (((i % 5) == 0) and ((i % 7) == 0)):
        print(i, "chickenmonkey")
    elif ((i % 5) == 0):
        print(i, "chicken")
    elif((i % 7) == 0):
        print(i, "monkey")
    else:
        print(i)