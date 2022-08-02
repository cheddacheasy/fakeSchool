import random
import string
from random import seed, randint
import names
from typing import Optional, List, Dict
import pandas as pd


# generates random password for the student
def password() -> str:
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.digits
    length = 10
    password_build = lower + upper + num + symbols
    temp = random.sample(password_build, length)
    password_final = "".join(temp)
    return password_final


def full_name() -> str:
    name = names.get_full_name()
    return name


def institution() -> str:
    school_list: List[str] = []
    # open the file
    data = pd.read_csv("../Institutions/us_universities.csv")
    school_list = data['name'].tolist()
    return random.choice(school_list)


# email format take url from file and strip to format
def stud_email(student_name: Optional[str] = None) -> str:
    student_email: str
    url_list: List[str] = []
    extension_list: List[str] = []
    sep: str = ".edu"
    sep2: str = ".org"
    sep3: str = ".com"

    # open the file
    data = pd.read_csv("Institutions/us_universities.csv")
    url_list = data['url'].tolist()

    for index, item in enumerate(url_list):
        strip_url = url_list[index][11:-1]
        if sep in strip_url:
            strip_url2 = strip_url.split(sep, 1)[0]
            strip_url2 = strip_url2 + sep
        if sep2 in strip_url:
            strip_url2 = strip_url.split(sep, 1)[0]
            strip_url2 = strip_url2 + sep2
        if sep3 in strip_url:
            strip_url2 = strip_url.split(sep, 1)[0]
            strip_url2 = strip_url2 + sep3
        extension_list.append(strip_url)

    if student_name is None:
        student_name = full_name()
    extension = random.choice(extension_list)
    student_email = student_name.replace(" ", "") + extension
    print(student_email)
    return student_email


def student_id_number() -> int:
    student_number: int
    student_id: str

    student_number = random.randint(100000, 999999)
    # student_id = school_letter + str(student_number)

    return student_number

def student_status() -> str:
    status: str
    credit_status: Dict[str] = {}

    credit_status = {
        "Full time": 12,
        "3/4 time": 9,
        "Part time": 6,
        "Less than half": 1
    }

    status = random.choice(list(credit_status))
    return status


def student_credit_hours(credit_status: str) -> int:
    credit_hours: int


    match credit_status:
        case "Full time":
            credit_hours = random.randint(12, 18)
        case "3/4 time":
            credit_hours = random.randint(9, 11)
        case "Part time":
            credit_hours = random.randint(6, 8)
        case "Less than half": credit_hours = random.randint(1, 5)
    return credit_hours

def student_gpa() -> int:
    gpa: int
    student_type: List[str]
    letter_grade: str

    student_type = [
        "good student", "average student", "below average student"
    ]

    letter_grade = random.choice(student_type)
    match letter_grade:
        case "good student":
            gpa = round(random.uniform(3.00, 4.00), 2)
        case "average student":
            gpa = round(random.uniform(2.00, 4.00), 2)
        case "below average student":
            gpa = round(random.uniform(1.00, 2.00), 2)
    return gpa


def student_Degree() -> str:
    degree: List[str]
    degree_choice: str

    degree = [
        "Associate", "Bachelor", "Doctorate", "Vocational", "Post-Doctorate"
    ]

    degree_choice = random.choice(degree)

    return choice

def student_year() -> str:
    year_choice: List[str]
    year_status: str

    year_choice = [
        "Freshman", "Sophmore", "Junior", "Senior"
    ]
    
    year_status = random.choice(year_choice)
    return year_status

