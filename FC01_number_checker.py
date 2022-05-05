# function here

def num_check(question, error, num_type):
    valid = False
    while not valid:
        
        # ask user for number and check it is valid
        try:
            response = num_type(input(question))
            
            if response <= 0:
                print(error)
            else:
                return response
        # if an integer is not entered, display an error
        except ValueError:
            print(error)

# main routine goes here

get_int = num_check("How many do you need? ","Please enter an amount more than 0\n", int)

get_cost = num_check("How much does it cost? $ ", "Please enter an amount more than 0\n", float)

# print results
print("You need: {}".format(get_int))
print("It costs: ${}".format(get_cost))