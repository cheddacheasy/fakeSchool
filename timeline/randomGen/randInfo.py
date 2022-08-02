"""
puts everything together for genereating random data
for the students and the counselors.
"""

from randomFile import randomStudFileCSV, randStudData
from randAdmin import randAdmineCSV




def main()->None:
    print("Hello")
    if randAdmineCSV() is True:
        print("Succesfully created the Counselor fake data")
        print("Check for 'randAdmin.csv'")
    studCList = randomStudFileCSV()
    if randStudData(studCList) is True:
        print("Succesfully created the Counselor fake data")
        print("Check for 'random.csv' and 'randomStudData.csv'")







if __name__ == '__main__':
    main()
