class Functions:
    def encrypt(message, shift):
        encrypted_message = "" #Defines it as an empty string
        encryptedMessage = "" #Defines it as an empty string
        cap = 0 #Defines cap as 0
        for ch in message.lower(): #This takes each letter of the message
            if ch.isalpha(): #If the message has a character, it's passed through. This stops the ascii code of a space getting mixed up in the code.
                ch = ord(ch) #Changes the letter into its corrasponding Ascii code
                ch += int(shift) #Adds the shift
                
                
                
                if ch > ord("z"): #Sees if the Ascii is now bigger than the last letter in the alphabet
                    while ch > ord("z"): #This ensures that the code, if given a really big shift, isn't too big
                        ch -= 26 #Takes away 26 as there are only 26 letters, therefore it'll go back to 'a'
                    encryptedMessage += chr(ch) #This adds to the newly altered message
                else:
                    encryptedMessage += chr(ch) #This adds the characters that weren't greater than 'z'
            else:
                encryptedMessage += ch #This adds a character that isn't a letter, eg. A space, period, etc.
        for letter in encryptedMessage: #This for loop capitalizes the first letter of the sentence
            cap += 1 #Adds one to 'cap' every time the loop finishes once
            if cap == 1: #If cap is equal to 1 - the following happens
                encrypted_message += letter.upper() #As cap is equal to one, this is the first letter, so it's placed into the string as a capital letter
            else: #If cap is not equal to 1 - this happens
                encrypted_message += letter.lower() #As I've already placed a capital letter, the rest should be lower case
        return encrypted_message #The functions returns the punctuated and decrypted message
class Menu: 
    displayMenu = True
    while displayMenu == True: 
        menu = input("""
1) Encrypt
2) Exit
""") 
# <<<<<<<<<<<<<<<<<<<<<<<<<<<< main component >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



        if menu == '1': #This is where the encrypt function gets its variables
            storeEncryptedMessages = open("encryptedMessages.txt", "a") #Opens the file 'encryptedMessages.txt' and assigns it to the corresponding variable
            message = input("What is the message that you'd like to encrypt? ") #Message to encrypt
            shift = input("What is the shift? ") #The shift for the message
            enctpMessage = Functions.encrypt(message, shift) #Calls the encrypt function from 'Functions'
            print(enctpMessage)
            storeEncryptedMessages.write("The original message was '" + message + "' with a shift if '" + shift + ".' The encrypted message was '" + enctpMessage + ".' \n") #Writes into the file
            storeEncryptedMessages.close() #Closes the file
        elif menu == '2': 
            print("Finished")#This exits the loop that runs the menu, therefore, closing the application the program
            break #This breaks the while
        elif menu == "exit":
            break

