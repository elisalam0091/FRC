def yes_no(question, instuctions):

    to_check = ["yes", "no"]
    
    instruction = 'Enter 1 to Encrypt a message', 'Enter 2 to Decrypt a message', 'Enter 3 to exit'
    Valid = False
    while not Valid:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item 

        print("Please enter either yes or no...\n")


# prints in terminal and returns input
want_help = yes_no("Do you want to read the instructions? ", "Enter 1 for Encrypt, Enter 2 for Decrypt, Enter 3 to Exit") 
print("You said '{}'\n".format(want_help))
