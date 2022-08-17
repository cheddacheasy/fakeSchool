import functions as fc


"""
    The purpose of this module is to add a csv module for the fake data module I created
    This will be the first step in creating a gui to create many types of random generated
    spreadsheets
"""






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

def menuSwitchBoard(userChoice: int) -> int:
    """
        Receives the user input choice in regards of what they would like to choose to put 
        in their csv file

                parameters:
                    userChoice (int) : represents user choice for what will be put in csv file
                return:
                    UserChoice (int) : represents the user choice for name randomization 
    """

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

# may need to figure out where this goes
def buildFile(nameChoice: int)->bool:
    """
            Receives the user input choice in regards of what they would like to choose to put 
            in their csv file

                    parameters:
                        userChoice (int) : represents user choice for what will be put in csv file
                    return:
                        UserChoice (int) : represents the user choice for name randomization 
    """

    # header creation
    # actuall adding info from the file
    pass


def headerPrompt(nameChoice: int) -> None:
    """
            Receives nameChoice which represents what the user wants listed in their file header: first names, last names, or both

                    parameters:
                        nameChoice (int) : represents user choice for what will be put in csv file header
                    return:
                        UserChoice (int) : represents the user choice for name randomization 
    """

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
    # may move this to inside header build or make another function for it
    values = headerBuild(testName2, nameChoice)
    if values[0]:
        print("Filename ", values[1])
    else:
        print("Error in generating file header")


def headerBuild(headerTitle: str, nameChoice: int) -> list[bool, str]:
    """
        Receives headerTitle which is the file name given by user and nameChoice build the csv file header

                parameters:
                    headerTitle (str) : users choice for the csv file name
                    nameChoice (int) : users choice of header first name, last name, or both
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


