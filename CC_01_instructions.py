def yes_no(question):

    to_check = ["yes", "no"]
    
    Valid = False
    while not Valid:

        response = input(question).lower()

        for item in to_check:
            if response == item:
                return response
            elif response == item[0]:
                return item
        print("Please enter either yes or no...\n")

# prints in terminal and returns input
want_help = yes_no("Do you want to read the instructions? ")
print("You said '{}'\n".format(want_help))




