# function
def yes_no(question):

    to_check = ["yes", "no"]
    
    Valid = False
    while not Valid:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item

        print("Please enter either yes or no...\n")

# loop for testing purposes
for item in range(0,6):
    want_help = yes_no("Do you want to read the instructions? ")
    print("You said '{}'\n".format(want_help))