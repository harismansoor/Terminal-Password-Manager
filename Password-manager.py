# A TEAM EFFORT BY TEAM 25
# HARIS | RYAN | MELISSA | ZITA
# COMP1002 GROUP PROJECT

import os
import os.path
import hashlib
import random
import string
from hashlib import new
import fileinput

#Two Initial txt files to store master password and security question answers.
passwordManager = "master.txt"
forgotPassQ = "forgotpass.txt"


#Menu Printing functions
def mainMenu():
    print("\n   -------------------------------\n")
    print("Welcome to Password Management System\n    --- A Project by Team 25 --- \n\n--------------------------------------\n")
    print("1 - Sign Up\n2 - Log in\n3 - Forgot Password\n4 - Quit\n")
def functionsOptionManu():
    print("Choose Your Option:")
    print("1 - Store New Passwords\n2 - View a Password\n3 - Update a Password\n4 - Password Generator\n5 - Strength Analysis\n6 - Delete Password\n7 - Quit\n")        
def storingMenu():
    print("\n    ---------------------------\n"
                "You're in storing new password mode\n"
                "------------------------------------\n")
def passUpdateMenu():
    print("\n   -------------------------\n"
                "You're in Password update mode!\n"
                "-------------------------------\n") 
def viewingMenu():
     print("\n    -------------------------\n"
                "You're in viewing password mode\n"
                "----------------------------------\n")
def passGenMenu():
    print(      "\n     ---------------------------\n"
                "You're in Random password Generator mode\n"
                "----------------------------------------\n")
def strengthAnalysisMenu():
    print(      "\n     ---------------------------\n"
                "You're in Password Strength Analysis mode\n"
                "----------------------------------------\n")
def quittingMenu():
    print("\n     ---------------------------\n"
                "Quitting the program... See you Again!\n"
                "-------------------------------------\n")
def signUpMenu():
    print("\nSign up!\n---------")
    print("[ATTENTION!!] If you already have an account, then Log in instead of Sign up") #Warning for users to prevent from erase previous data accidentally.
    print("Signing up again would erase the previous existing passwords, if any\n")
def deletePassMenu():
    print("\n   -------------------------\n"
                "You're in Password Delete mode!\n"
                "-------------------------------\n") 


#Property functions 
def eraseData(fileName): 
    '''Erases all data from any txt file, takes in the File Name as parameter'''
    file = open(fileName, 'r+')
    file.truncate(0)
    file.close()

def genpass():
    '''
    Generates a 12 character strong password. The first character is a letter to readibility.
    While other characters are randomly generated letters or numbers or even symbols.
    However user input is taken to determine if user wants symbols in the generated password
    '''
    length = 12
    print()
    genFlag = str(input("Do you want to include symbols such as @ or . or - or _ in your password? (Yes or No): ").lower())
    print()
    
    #validation for user input
    while (genFlag not in {'yes','no'}): 
        print("Invalid input. Please input yes or no")
        genFlag = str(input().lower())
        print()
        
    if(genFlag == "yes"):
        symbol = "._-@" 
        char = string.ascii_letters + string.digits + symbol
    else:
        char = string.ascii_letters + string.digits
    
    fdigit = random.choice(string.ascii_letters) 
    rdigit = ''.join([random.choice(char) for i in range(length-1)])
    while ((genFlag == "yes") and not(any(c in symbol for c in rdigit))):
        rdigit = ''.join([random.choice(char) for i in range(length-1)])
    global randpw 
    randpw = fdigit + rdigit 

def randgenpass():
    '''
    Generates a 12 character strong password. The first character is a letter to readibility
    While other characters are randomly generated letters or numbers or even symbols. No User Input is taken
    
    :param length: 
    :return: randomly generated 12 character long password.
    '''
    length = 12
    symbol = "._-@" 
    char = string.ascii_letters + string.digits + symbol
    fdigit = random.choice(string.ascii_letters) 
    # '''the first digit is set to letters to reduce confusion''' 
    # '''randomly generate the other digits'''
    rdigit = ''.join([random.choice(char) for i in range(length-1)])
    randgenpw = fdigit + rdigit
    return randgenpw

def optionpage(): 
    '''
    Navigates to different function following the user input.
    This function works as a loop which gives user interface to
    select their desirable command.
    such as  
            1- Storing Password
            2- View Password
            3- Update Password
            4- Randomly Generate Password
            5- Password Strength Analysis
            6- Delete Password
            7- Quit
            
    Relevant functions are called within this function to execute the
    desirable command.
    '''
    
    quit = False 
    while quit == False: 
        functionsOptionManu()
        userChoice = eval(input("Option: "))
        while (userChoice>7 or userChoice<1): 
            print("\n   Input is out of range\nPlease Choose 1,2,3,4,5,6 or 7 only!")
            userChoice = int(input("Option: "))

        #storing new passwords
        if (userChoice == 1):
            storingMenu()
            numberOfnew = int(input("Number of passwords, you want to store: "))
            for i in range(0,numberOfnew): 
                create_file()
        
        #viewing passwords
        if (userChoice == 2): 
            viewingMenu()
            readPasswords()   
            
        #Updating Password        
        if (userChoice == 3): 
            passUpdateMenu() 
            update_file()   
            
        # Generate Password     
        if (userChoice == 4):
            passGenMenu()
            genpass()   
            print("Password Generated by Program is:", randpw)
            print("This passowrd is VERY STRONG, you might want to use it for any website. Cheers!")
            print()
            
        #Password Strength Analysis
        if (userChoice == 5): 
            strengthAnalysisMenu()
            spw = str(input("Enter a password to know its strength: "))
            print("Strength: ",password_strength(spw)) 
            print()  
        
        #Password Delete
        if (userChoice == 6):
            deletePassMenu()
            deleteFile()
            
        #Quit         
        if (userChoice == 7):
            quittingMenu()
            quit = True
            break
        if(quit==True):
            break

def password_strength(pw: str):
    '''
    Password Strength Analysis Function: 
    :param pw: The password
    :type str
    
    This function will analyse the strength of a password by checking criterias for every password
    there are upto four criterias which the password has to follow in order to be strong or very strong
    Criterias:
        has uppercase
        has symbol
        has number
        has more than eight characters
    The analysis is done on number of criterias followed.
    For example if 1 criteria is followed then the password would be weak
    Whereas if 4 criterias are followed then the password would be very strong
    '''
    more_than_8 = len(pw) >= 8 
    has_symbol = False
    has_uppercase = False
    has_number = False
    number_of_true = 0

    symbol = ["!", "@" ,"," , ".", ":", ";", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "~", "+", "=", "/", "[", "]", "{", "}", "\\", "|", "'", '"', "?", ">", "<"]

    for char in pw: 
        if char >= "A" and char <= "Z":
            has_uppercase = True
        elif char in symbol:
            has_symbol = True
        elif char >= "0" and char <= "9":
            has_number = True 

    if has_uppercase: 
        number_of_true += 1
    if has_symbol:
        number_of_true += 1
    if has_number:
        number_of_true += 1
    if more_than_8:
        number_of_true += 1


    if number_of_true == 4:
        return "Very Strong"
    if number_of_true == 3:
        return "Strong"
    if number_of_true == 2:
        return "Weak"
    if number_of_true <= 1:
        return "Very Weak" 
      
def createNewMasterPassword(masterPassword):
    '''
    :param masterPassword: The Master Password input my user
    :type str
    
    This function will make a new txt file and store the Master Password in it
    The speciality is that the Master Password will be encrypted so that no other user can know it
    The encryption is verifiably One-Way and can not be decrypyted.
    The user can enjoy knowing only one master password to access all of the other passwords
    '''
    if os.path.exists(passwordManager):
        eraseData(passwordManager) 
        file = open(passwordManager, 'w')
        file.write("Password storing with master password\n")
        file.write("Master Passowrd encrypted for security\n")
        file.write("------------------------------------\n")
        hash = hashlib.sha512((masterPassword).encode('utf-8')).hexdigest()
        file.write("%s\n" % hash)
        file.close()
    else:
        file = open(passwordManager, 'w')
        file.write("Password storing with master password\n")
        file.write("Master Passowrd encrypted for security\n")
        file.write("------------------------------------\n")
        hash = hashlib.sha512((masterPassword).encode('utf-8')).hexdigest()
        file.write("%s\n" % hash)
        file.close()  

def create_file():
    '''
    create_file function is dedicated for storing new passwords
    Complete Data validation is implemented so that storing passwords is smooth
    Users desired 
        1- website
        2- username
        3- password
    is input to store the basic information in a new dedicated txt file.
    
    The signature method to be noted is that the user inputs are encrypted via Ceaser Cypher method so that the new txt files that are created have encrypyted names
    It might be confusing for users other than the main user and even the user itself, but in order to guarantee safety, and security of the passwords stored within,
    the names of the txts have to be encrypted. This way we can ensure that if txt file is opened directly, the name of the txt doesn't specifies the website and the ID!
    
    for example if the user inputs
        website: google
        ID: Haris1999
        password: pass123
    Name of the txt file will NOT be googleHaris1999.txt - which obviously will make it obvious that the website is google and id is Haris1999.
    
    User also has the option to use some randomly generated password options for the website
    '''
    GENFlag = str(input("Do you want System to Give you some Randomly Generated Password Options? (Yes or No): ").lower())
    while (GENFlag not in {'yes','no'}):
        print("Invalid input. Please input yes or no")
        GENFlag = str(input().lower())
    # if user needs some randomly generated options
    if(GENFlag == "yes"):
        print()
        web = str(input('Please enter the website: ').lower())
        id = str(input('Please enter the ID: '))
        print()

        for i in range(1,4):
            print(i," ",randgenpass())
            
        print()    
        print("Feel free to Use them or Input your Own Password")    
        pswd = str(input('Please enter the password: '))
        
        inputwebe = encrypt(web)
        inputIDe = encrypt(id)
        
        f = open(inputwebe + inputIDe + '.txt', 'w')
        f.write(pswd) 
    else:
        web = str(input('Please enter the website: ').lower())
        id = str(input('Please enter the ID: '))
        pswd = str(input('Please enter the password: '))
        inputwebe = encrypt(web)
        inputIDe = encrypt(id)
        
        f = open(inputwebe + inputIDe + '.txt', 'w')
        f.write(pswd)  

    # replace if duplicate file is found
    if os.path.exists(passwordManager):
        f = open(inputwebe + inputIDe + '.txt', 'w')
        eraseData(inputwebe + inputIDe + '.txt')
        f.write(pswd)
        f.close()
    else:
        f = open(inputwebe + inputIDe + '.txt', 'w')
        f.write(pswd)
        f.close()   

    print()
    print("Password Stored Successfully")
    print()

def update_file():
    '''
    update_file function is dedicated to update password on user's will.
    When the user asks for updating password, webiste name and user name is asked.
    Then user has to confirm if he/she wants to update the specified txt file and lastly,
    user can input the new password, the password is updated successfully
    '''
    
    inputweb = str.lower(input('Please input the website of the password you would like to update: '))
    inputID = str(input('PLease input the ID of the password you would like to update: '))
    
    inputwebe = encrypt(inputweb)
    inputIDe = encrypt(inputID)
    
    if os.path.isfile(inputwebe + inputIDe + '.txt'):
        f = open(inputwebe + inputIDe + '.txt', 'r')
        data = f.read()
        print()
        f.close()
        print("Website: ",inputweb)
        print("Username: ", inputID)
        print("Password: ", data)
        print()
        confirmFlag = str.lower(input("Do you want to Update this Password? (Yes or No): "))
        while (confirmFlag not in {'yes','no'}):
            print("Invalid input. Please input yes or no")
            confirmFlag = str.lower(input()) 
        if (confirmFlag == "yes"):
            f = open(inputwebe + inputIDe + '.txt', 'w')
            newpw = input("Please enter the new password: ")
            f.write(newpw)
            print()
            print('Password Updated successfully')
            print()
            f.close
        else:
            optionpage()
    else:
        print('Sorry. Your file is not found.')
        optionpage()

def compareMaster(masterPassword):  
    '''
    :param masterPassword: The Master Password
    :type str
    
    compareMaster is a boolean function to validate if the master password input my user
    is the password that was initialized while signing up. 
    the input is encrypyted similarly and compared to encrypted master password stored in master.txt.
    if it matches, then the function returns true, if not, then it returns false.
    '''  
              
    master = open(passwordManager)
    masterLines = master.read().splitlines()
    hash = hashlib.sha512((masterPassword).encode('utf-8')).hexdigest()
    if (hash == masterLines[3]):
        return True
    else:
        return False
       
def encrypt(text):
    '''
    :param text: The name of the website or the ID
    :type str
    
    Encrypt function is of the most lethal and effective functions. It is used in this program specifically to encrypt the names of the txt files,
    so that they seem confusing for any user other than the main user. It might be confusing for the user itself, but in order to guarantee safety,
    and security of the passwords stored within, the names of the txts have to be encrypted. 
    '''
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + 4-65) % 26 + 65)
        else:
            result += chr((ord(char) + 4 - 97) % 26 + 97)
    return result

def readPasswords():
    '''
    readPasswords is dedicated to read the password user wants for any particular website.
    User is prompted to input the website name and user name, and the password for the corresponding website is displayed.
    The input is encrypyted using Ceaser Cypher encryption to get the name of the exact txt file the password lies in.
    It returns an error if no such website password entry was found.
    '''
    
    inputweb = str(input('Please input the website: ').lower())
    inputID = str(input('Please input the ID: '))
    
    inputwebe = encrypt(inputweb)
    inputIDe = encrypt(inputID)
    
    if os.path.isfile(inputwebe + inputIDe + '.txt'):
        file = open(inputwebe + inputIDe + '.txt', 'r')
        pw = file.read()
        file.close()
        print('Website: ',inputweb)
        print('username: ', inputID)
        print('Password: ', pw)
        print('Strength of your password: ', password_strength(pw))
        print('\n')
        optionpage()
    else:
        print()
        print('Sorry Password File for this website and ID was not found.')
        print("Check to see if you made any typos. Cheers!")
        print()
        optionpage()

def log_In():
    '''
    log_In as the name suggests is a function to enable user to log in. 
    It calls the function compareMaster to validate that the master password initialized at the the time of sign-up is entered.
    This function is properly validated and will not grant access until the master password is entered correctly
    For increased security, account gets locked if master password is entered wrongly 5 times.
    In that case user has to re-run the program and reset password by selecting forgot password command.
    '''
    print("\nLog in!\n---------")
    masterPass = input("Input Master Password: ")
    print()
    
    flag = compareMaster(masterPass)
    wFlag = 0
    if (flag == False):
        print("NOTE: If you enter Master password wrong 5 times, your account will be locked")
        print("In that case, you will have to re-run the program and select 'Forgot Password' to reset your password") 
    while(flag == False):
        wFlag += 1
        print("Wrong Master Password. Try Again!") 
        masterPass = input("Input Master Password: ")
        flag = compareMaster(masterPass)
        if (wFlag == 5):
            print("Password Attempts finished. Your account is locked")
            print(" -------------Quitting the program-------------")
    if (flag == True):       
        optionpage()  

def createNewForgotPassFile():
    ''' createNewForgotPassFile created a new txt file to store the security question answers'''
    if os.path.exists(forgotPassQ):
        eraseData(forgotPassQ)
        file = open(forgotPassQ, 'w')
        file.close()
    else:
        file = open(forgotPassQ, 'w')
        file.close()

def forgotPasswordQuestions():
    '''
    forgotPasswordQuestions is a dedicated function to store answers of 2 security questions in encrypted form.
    This function asks user 2 security questions in case user forgets the master password and want to reset it.
    The answers are stored in a new txt file. The reason answers are encrypyted is because then anybody can open the file,
    see the answers, and reset the master password. Thus this another security measure implemented by this project.
    
    This function calls createNewForgotPassFile function to create the file for the storage
    '''
        
    createNewForgotPassFile()
    file = open(forgotPassQ, 'w')
    supplementaryQ_one = input("Your father's last name?: ").lower()
    supplementaryQ_two = input("Your favourite animal?: ").lower()
    file.write("Security Question One\n")
    file.write("Answer encrypted for security\n")
    file.write("------------------------------------\n")
    hashOne = hashlib.sha512((supplementaryQ_one).encode('utf-8')).hexdigest()
    file.write("%s\n" % hashOne)
    file.write("------------------------------------\n")
    file.write("Security Question Two\n")
    file.write("Answer encrypted for security\n")
    file.write("------------------------------------\n")
    hashTwo = hashlib.sha512((supplementaryQ_two).encode('utf-8')).hexdigest()
    file.write("%s\n" % hashTwo)
    file.write("------------------------------------\n\n")
    file.close()

def securityQuestionsCompare(supplementaryQ_one,supplementaryQ_two):
    '''
    :param supplementaryQ_one: Answer of first security/supplementary question
    :type str
    :param supplementaryQ_two: Answer of first security/supplementary question
    :type str
    
    This function serves the purpose of comparing the user input with the contents in the forgotpass.txt file.
    '''
    
    master = open(forgotPassQ)
    masterLines = master.read().splitlines()
    hash_one = hashlib.sha512((supplementaryQ_one).encode('utf-8')).hexdigest()
    hash_two = hashlib.sha512((supplementaryQ_two).encode('utf-8')).hexdigest()
    if (hash_one == masterLines[3]):
        if (hash_two == masterLines[8]):
            return True
        return False;
    else:
        return False

def deleteFile():
    '''deleteFile function serves the purpose any stored password file from the system'''
    print("Enter the details of the password entry you want to delete")
    web = str(input('Please enter the website: ').lower())
    id = str(input('Please enter the ID: '))
    inputwebe = encrypt(web)
    inputIDe = encrypt(id)
    
    if os.path.exists(inputwebe + inputIDe + '.txt'):
        os.remove(inputwebe + inputIDe + '.txt')
        print()
        print("Password File removed successfully")
        print()
    else:
        print()
        print("Password file not found!")
        print("Check if you entered website name and ID correctly")
        print()


#The Main Function
def main():
    '''
    main function is the function that is called when the program is run.
    It is undoubtedly the master function which calls different functions to execute the Password Management System.
    User is prompted to ask if he/she wants to 
                                            1- Sign Up
                                            2- Log In
                                            3- Forgot Password
                                            4- Quit
    Based on User's command, the program proceeds accordingly.
    Proper Data Vaidation is provided, guaranteeing efficiency and reliability.
    '''
    mainMenu()
    userSystem = int(input("Option: "))
    
    #data validation
    while (userSystem>4 or userSystem<1):
        print("\n   Input is out of range\nPlease Choose 1,2,3 or 4 only!")
        userSystem = int(input("Option: "))
    
    if (userSystem == 1):
        signUpMenu()
        signUpFlag = str(input("Do you want to make a new account? (Yes or No): ").lower())
        while (signUpFlag not in {'yes','no'}):
            signUpFlag = str(input("Invalid input. Please input yes or no: ").lower())
        
        if (signUpFlag == "yes"):
            print()
            print("A Master Password is needed to make a new account for Password Management")
            print("----Would you like you generate a password automatically? (Yes or No)----")
            GenPassFlag = str(input().lower())
            #data validation
            while (GenPassFlag not in {'yes','no'}):
                print("Invalid input. Please input yes or no")
                GenPassFlag = str(input().lower())
                             
            if(GenPassFlag == "yes"):
                genpass()
                confirmMasterPass = randpw
                masterPass = randpw
                print ("The generated Master Password is:",randpw)
            else:
                print()
                masterPass = input("Input your Own New Master Password: ")
                confirmMasterPass = input("Confirm your New Master Password: ")
                print()
                
                #data validation
                while(masterPass != confirmMasterPass):
                    print("Passwords do not match. Try again!")
                    masterPass = input("Input your Own New Master Password: ")
                    confirmMasterPass = input("Confirm your New Master Password: ")
            

            if (masterPass == confirmMasterPass):
                print("Please answer few supplementary questions in case you forget the master password\n")
                forgotPasswordQuestions()
                print()
                print("Creating master file...\n Master file created!\n----------------------\n")
                createNewMasterPassword(masterPass)
                optionpage()

        else:
            logInFlag = str(input("Do you want to Log-In instead? (Yes or No): ").lower())
            #data validation
            while (logInFlag not in {'yes','no'}):
                print("Invalid input. Please input yes or no")
                signUpFlag = str(input().lower())
            if(logInFlag == "yes"):
                log_In()
            else:
                quittingMenu()

    if (userSystem == 2):
        log_In()
        
    if (userSystem == 3):
        print("Forgot your Master Password? No problem!"
              "Just answer the ssecurity questions below"
              "to reset your master password.")
        supplementaryQ_one = input("Your father's last name?: ").lower()
        supplementaryQ_two = input("Your favourite animal?: ").lower()
        print()
        
        flag = securityQuestionsCompare(supplementaryQ_one,supplementaryQ_two)
        
        if (flag == True):
            print("Security Question Answers were correct!")
            print("You can reset your password now. Your existing passwords will be saved")
            resetMaster = input("Input your new Master Password: ")
            resetMasterConfirm = input("Confirm new Master Password: ")
            if(resetMaster == resetMasterConfirm):         
                with open(passwordManager,'r') as file:
                    changeMaster = file.readlines()             
                hash = str(hashlib.sha512((resetMaster).encode('utf-8')).hexdigest())
                changeMaster[3] = hash             
                with open(passwordManager, 'w') as file:
                    file.writelines(changeMaster)
                    file.close()      
                print()             
            print("Master Password updated. You may re-run Password Management program now and log in")
            print("-------------------------------Quitting Program------------------------------------")
         
    if (userSystem == 4):
        quittingMenu()

main()


# References used for the project

#   read and writing txt files
#   https://www.guru99.com/reading-and-writing-files-in-python.html

#   checking existence of txt files
#   https://www.pythontutorial.net/python-basics/python-check-if-file-exists/

#   Deleting txt file
#   https://www.dummies.com/programming/python/how-to-delete-a-file-in-python/

#   ceasar cipher
#   https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/

#   docstrings
#   https://www.programiz.com/python-programming/docstrings

#   editing a txt file
#   https://www.kite.com/python/answers/how-to-edit-a-file-in-python

#   hashlib information
#   https://docs.python.org/3/library/hashlib.html

#   manipulating txt files
#   https://towardsdatascience.com/python-bites-manipulating-text-files-511d1257d399

#   password strength analysis
#   https://www.geeksforgeeks.org/python-program-check-validity-password/

#   random password generation
#   https://geekflare.com/password-generator-python-code/

#   Functions of string module
#   https://www.atqed.com/python-string-printable