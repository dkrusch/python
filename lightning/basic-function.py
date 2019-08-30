# * Write a function that takes a list, a number, and a string as args.
# * The string parameter should have a default value.
# * In the function body, loop over the list and print the items, each one prefaced by the value of the string argument
#    * One example output might then be "I have visited the city of San Francisco" if "San Francisco" was an item in the list, and the string argument was "I have visited the city of "
# * Try it out! Execute the function both with and without passing in a value for the string parameter

def create_string(*args):
    default_string = "What doth"

    if len(args) > 1:
        default_string = args[1]

    # for argument in args:
    #     if isinstance(argument, list):
    #         city_list = argument
    #     else:
    #         default_string = argument

    for city in args[0]:
        if default_string == "What doth":
             print(f"{default_string} {city}?")
        else:
            print(f"{default_string} {city}.")

def create_stringo(cities, default_string="What doth"):
    for city in cities:
        if default_string == "What doth":
             print(f"{default_string} {city}?")
        else:
            print(f"{default_string} {city}.")

create_string(["San Fran", "New York", "Nashville", "Asheville"], "I will endeavour to pursue a potential visit to")
create_string(["San Fran", "New York", "Nashville", "Asheville"])

create_stringo(["San Fran", "New York", "Nashville", "Asheville"], "I will endeavour to pursue a potential visit to")
create_stringo(["San Fran", "New York", "Nashville", "Asheville"])