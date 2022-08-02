'''
This file is responsible for generating the random counselor csv
Fields include:
    First Name
    Last Name
    Counselor Number
    Counselor Password
    Assigned Student Lettering
'''

# imports and libraries used
from random import seed, randint
import random
import string
import csv
from csv import writer
import names


# creates admin header on the csv file
def createAdminFile()->None:
    header = ['First name', 'Last name','Admin#', 'Admin Password', 'student lettering']
    with open('randomAdmin.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)

# generate randome password
def randPass()->str:
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits 
    symbols = string.digits 
    length = 10
    all = lower + upper + num + symbols

    temp = random.sample(all, length)

    password = "".join(temp)

    return password

# generates Counselor Id number
def Adminnum()->int:
    number =  randint(99999, 999999)
    return number

# genereate random Name for counselor
def randName()->str:
    name = names.get_full_name()
    return name

# puts data into the admin csv
def randAdmineCSV()->bool:
    createAdminFile()
    i=0
    seed(1)
    while i < 6:
        name = randName()
        fName = name.split()[0]
        lName = name.split()[1]
        adNum = Adminnum()
        adNum = "A00"+str(adNum)
        studAssign = ["ABCD", "EFGH", "IJKLM", "NOPQ", "RSTU", "VWXYZ"]
        password = randPass()
        infolist = [fName, lName, adNum, password, studAssign[i]]
        with open('randomAdmin.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(infolist)
        i+=1
    f_object.close()
    return True
def main():
    randAdmineCSV()

if __name__ == '__main__':
    main()
