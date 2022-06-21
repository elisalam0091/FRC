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

    def decrypt(message, shift):
        nDecryptedMessage = ""
        decryptedMessage = ""
        cap = 0
    
        for ch in message.lower(): #This takes each letter of the message
            if ch.isalpha(): #If the message has a character, it's passed through. This stops the ascii code of a space getting mixed up in the code.
                ch = ord(ch) #Changes the letter into its corrasponding Ascii code
                ch -= int(shift) #Takes away the shift
                if ch < ord("a"): #Sees if the Ascii is now less than the first letter in the alphabet
                    while ch < ord("a"): #This ensures that the code, if given a really big shift, isn't too small
                        ch += 26 #Adds 26 as there are only 26 letters, therefore it'll go back to 'z'
                    decryptedMessage += chr(ch) #This adds to the newly altered message
                else:
                    decryptedMessage += chr(ch) #This adds characters that weren't less than 'a'
            else:
                decryptedMessage += ch #This adds a character that isn't a letter, eg. A space, period, etc.
        for letter in decryptedMessage: #This for loop capitalizes the first letter of the sentence
            cap += 1 #Adds one to 'cap' every time the loop finishes once
            if cap == 1: #If cap is equal to 1 - the following happens
                nDecryptedMessage += letter.upper() #As cap is equal to one, this is the first letter, so it's placed into the string as a capital letter
            else: #If cap is not equal to 1 - this happens
                nDecryptedMessage += letter.lower() #As I've already placed a capital letter, the rest should be lower case
        return nDecryptedMessage #The functions returns the punctuated and decrypted message
print()
print("Welcome to Caesar Chiper")

class Menu: #This is a class designed just to run the menu. This helps to make the code look tidy
    displayMenu = True #If this variable
    while displayMenu == True: #While true, this runs the menu before it's broken
        menu = input("""
1) Encrypt
2) Decrypt
3) Exit
""") #Menu input which is made by the user to choose from one of the selections in the menu by addressing it by the number to the left of the action
        if menu == '1': #This is where the encrypt function gets its variables
            storeEncryptedMessages = open("encryptedMessages.txt", "a") #Opens the file 'encryptedMessages.txt' and assigns it to the corrasponding variable
            message = input("What is the message that you'd like to encrypt? ") #Message to encrypt
            shift = input("What is the shift? ") #The shift for the message
            enctpMessage = Functions.encrypt(message, shift) #Calls the encrypt function from 'Functions'
            print(enctpMessage)
            storeEncryptedMessages.write("The original message was '" + message + "' with a shift if '" + shift + ".' The encrypted message was '" + enctpMessage + ".' \n") #Writes into the file
            storeEncryptedMessages.close() #Closes the file

        elif menu == '2': #This is where the decrypt function gets its variables
            storeDecryptedMessages = open("decryptedMessages.txt", "a") #Opens the file 'decryptedMessages.txt' to the corresponding variable
            message = input("What message do you want to decrypt? ") #Message to decrypt
            shift = input("What was the shift? ") #The shift
            DecryptedMessage = Functions.decrypt(message, shift) #Calls the decrypt function from 'Functions'
            print(DecryptedMessage)
            storeDecryptedMessages.write("The encrypted message was '" + message + ".' The decrypted message was '" + DecryptedMessage + "' with a shift of '" + shift + ".' \n") #Writes into this file
            storeDecryptedMessages.close() #Closes this file
        elif menu == '3': 
            print("Finished")#This exits the loop that runs the menu, therefore, closing the application the program
            break #This breaks the while
        elif menu == "exit":
            break
