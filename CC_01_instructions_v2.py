def yes_no(question):

    to_check = ["yes", "no"]
    instruction = "Press 1 for Encrypt, Press 2 for Decrypt, Press 3 to exit"
    Valid = False
    while not Valid:

        response = input(question).lower()

        for item in to_check:
            if input == to_check[0]:
                print(instruction)
            elif response == item[1]:
                return response
            print("Please enter either yes or no...\n")

# prints in terminal and returns input
want_help = yes_no("Do you want to read the instructions? ")
print("You said '{}'\n".format(want_help))






