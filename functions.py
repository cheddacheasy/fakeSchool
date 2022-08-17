'''
This will contain and hold all functions for the file creator,
The purpose of this file is to also be a rough outline for the 
Whole Lotta Fake application
'''

import string
import csv
import math
import random
from random import seed, randint
from csv import writer
import names
import sys
import os


# sex tells the function if you want a male, female, or no sex
def randFullName(sex: int) -> str:
    """
    returns a randomly generated first and last name based on sex.

            parameters:
                sex (int) : integer that represents the sex of the name
                    0 = male
                    1 = female
                    any other integer will produce a random male or femal full name

            return:
                name (str) : string of first and last name that represent a male or female sex
    """

    if sex == 0:
        name = names.get_full_name(gender='male')
    elif sex == 1:
        name = names.get_full_name(gender='female')
    else:
        name = names.get_full_name()
    return name


def randFullNameMain() -> None:
    """
    Creates a list of randomly generated full names
            parameters:
                None

            return:
                none
    """

    print("How many full names would you like to generate?")
    numNames = int(input(">"))
    namesList = []
    i = 0
    while i < numNames:
        randSex = random.randint(0, 2)
        testName = randFullName(randSex)
        i += 1


def randFirstName(sex: int) -> str:
    """
    returns a randomly generated first name based on sex.

            parameters:
                sex (int) : integer that represents the sex of the name
                    0 = male
                    1 = female
                    any other integer will produce a random male or femal full name

            return:
                name (str) : string of first name that represent a male or female sex
    """

    if sex == 0:
        name = names.get_first_name('male')
    elif sex == 1:
        name = names.get_first_name(gender='female')
    else:
        name = names.get_first_name()
    return name


def randFirstNameMain() -> list[str]:
    """
    returns a randomly generated list of first names based on sex.

            parameters:
                sex (int) : integer that represents the sex of the name
                    0 = male
                    1 = female
                    any other integer will produce a random male or femal full name

            return:
                name (str) : string of first name that represent a male or female sex
    """

    namesList = []

    print("How many first names would you like to generate?")
    numNames = int(input("> "))
    print("Choose from the following optios: ")
    print("Press 0                 All Male")
    print("Press 1                 All Female")
    print("Press 2                 All Random")
    nameType = int(input("> "))

    if nameType == 0:
        i = 0
        while i < numNames:
            testName = randFirstName(0)
            namesList.append(testName)
            i += 1
    elif nameType == 0:
        i = 0
        while i < numNames:
            testName = randFirstName(1)
            namesList.append(testName)
            i += 1
    elif nameType == 0:
        i = 0
        while i < numNames:
            randSex = random.randint(0, 2)
            namesList.append(testName)
            testName = randFirstName(randSex)
            i += 1

    return namesList


def randLastName() -> str:
    """
    returns a randomly generate last name based on sex.

            parameters:
                None
            return:
                name (str) : string of randomly generated last name
    """

    name = names.get_last_name()
    return name


def randLastNameMain() -> None:
    """
    returns a randomly generate list of last names based on sex.

            parameters:
                None
            return:
                name (str) : List of randomly generated last names
    """
    lastNames = []
    print("How many last names would you like to generate?")
    numNames = int(input(">"))
    i = 0
    while i < numNames:
        testName = randLastName()
        lastNames.append(testName)
        i += 1


def infoMenu() -> None:
    """
    Displays a list of options for the user can choose from for randomly generating
    names.
    The user can choose to randomlu generate first names, last names, full names,
    or mix first, last, and full names

            parameters:
                None
            return:
                None
    """

    print("Press 1: If you would like to get only first names")
    print("Press 2: If you would like to get only last names")
    print("Press 3: If you would like to get only full names")
    print("Press 4: If you would like to get a mix of first, last, and full names")
    print("Press 0: Exit")


def infochoice() -> int:
    """
    Receives the user input choice from the user in regards to their randomziation choice

            parameters:
                None
            return:
                UserChoice (int) : represents the user choice for name randomization 
    """

    UserChoice = int(input("> "))
    return UserChoice

# left off here
# finish documentation
# write out error handling 
# write out test for this file
def menuSwitchBoard(userChoice: int):
    if type(userChoice) != int or userChoice < 0 or userChoice > 5:
        raise ValueError("Invalid Choice")
    fileName = headerPrompt(userChoice)
    match userChoice:
        case 0:
            sys.exit("Exiting.... Have a nice day")
            return 0
        case 1:
            os.system('clear')
            randFirstNameMain()
            return 1
        case 2:
            os.system('clear')
            randLastNameMain()
            return 2
        case 3:
            os.system('clear')
            randFullNameMain()
            return 3

def buildFile(nameChoice: int)->bool:
    # header creation
    # actuall adding info from the file
    pass


def headerPrompt(nameChoice: int)->str:
    choice = 'N'
    while choice == 'n' or 'N':
        print("What will the name of the file be?")
        print("Reminder: YOU DO NOT INCLUDE CSV OR TXT EXTENSION")
        print("ex: randBankNames or randNames is acceptible format")
        testName = input("> ")
        # check 4th last spot for "." beginning of the extenstion
        if testName[-4] == '.':
            print("You added an extension accidentally.")
            testName2 = testName[:-4]
            print(f"Did you mean: ")
            print("Press Y: To confirm change")
            print("Press N: To re-enter new file name")
            choice = input(">")
            if choice == "Y" or choice == "y":
                break
            os.system('clear')
    values = headerBuild(testName2, nameChoice)
    if values[0]:
        print("Filename ", values[1])
    else:
        print("Error in generating file header")


def headerBuild(headerTitle: str, nameChoice: int) -> list[bool, str]:
    """
        Receives the user input choice from the user in regards to their randomziation choice

                parameters:
                    None
                return:
                    UserChoice (int) : represents the user choice for name randomization 
    """

    header = []
    needs = [True]
    # grab/create file name
    fileName = headerTitle + ".csv"
    match nameChoice:
        case 1:
            header.append("First Name")
            # first name only
        case 2:
            header.append("Last Name")
            # last name only
        case 3:
            header.append("First Name")
            header.append("Last Name")
            # first and last name 

    # open csv file and begin building the file
    with open(fileName, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
    fileName.close()
    needs.append(fileName)
    return needs

def main():
    headerPrompt()

if __name__ == '__main__':
    main()
