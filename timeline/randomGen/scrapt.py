import random

completters = ['A', 'B', 'C', 'D', 'F', 'I']
lettDict = {
    "A": "4",
    "B": "3",
    "C": "2",
    "D": "1",
    "F": "0",
}



gpa = 0
for letter in completters:
    if letter in lettDict.keys():
        gpa = int(lettDict[letter]) + gpa
        print("Yes in the dictionary: ",gpa)
classTot = 0
for _ in completters:
    if _ != 'I':
        classTot += 1
gpa = gpa / classTot

x = 0
while x< 6:
    print(random.choices(completters, k=8))
    x+=1

