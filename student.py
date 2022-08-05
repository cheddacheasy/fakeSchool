from dataclasses import dataclass, field
import randomFile
from faker import Faker
fake = Faker()

# add repr method maybe or leave it for person_info
@dataclass
class Person:
    """
    A class to represent administrative based student object


    Attributes
    ----------
    person_full_name : str
    first_name : str
    last_name : str
    student_id : int
    student_phone_number : int
    email : str
    student_ssid : str
    student_address : str

    Methods
    -------
    person_info(self) -> None
        Prints out all attributes of the person object
    """

    person_full_name: str = field(init=False)
    first_name: str = field(init=False)
    last_name: str = field(init=False)
    student_id: int = field(init=False)
    student_phone_number: str = field(init=False)
    email: str = field(init=False)
    student_ssid: str = field(init=False, repr=True)
    student_address: str = field(init=False)

    def __post_init__(self):
        """
        Constructs all the necessary attributes for the person object
        """

        self.person_full_name = randomFile.full_name()
        self.first_name = self.person_full_name.split()[0]
        self.last_name = self.person_full_name.rsplit(None, 1)[-1]
        self.email = randomFile.stud_email(self.person_full_name)
        self.student_id = randomFile.student_id_number()
        self.student_phone_number = fake.phone_number()
        self.student_ssid = fake.ssn()
        self.student_address = fake.address()

    def person_info(self) -> None:
        """ 
        display the administrative information of the student-person object
        generated

                parameters:
                    self: instance of student person object created

                return:
                    none
        """
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Email:", self.email)
        print("ID:", self.student_id)
        print("Phone Number: ", self.student_phone_number)
        print("SSID: ", self.student_ssid)
        print("Address: ", self.student_ssid)


@dataclass
class Student(Person): 
    """
    A class to represen the acadmeic based student object


    Attributes
    ----------
    college : str
    degree_type : str
    year_status : str
    college_hour_status : str
    current_credit_hours : int
    total_credit_hours : int
    student_gpa_current : float
    graduation_student_status : bool
    student_full_name : str

    Methods
    -------
    person_info(self) -> None
        Prints out all attributes of the person object

    college_info(self) -> None
        Prints out all attributes of the student object
    """

    college: str = field(init=False)
    degree_type: str = field(init=False)
    year_status: str = field(init=False)
    college_hour_status: str = field(init=False)
    current_credit_hours: int = field(init=False)
    total_credit_hours: int = field(init=False)
    student_gpa_current: float = field(init=False)
    graduation_student_status: bool = field(init=False)
    student_full_name: str = field(init=False)

    def __post_init__(self):
        """
        Constructs all the necessary attributes for the student object
        """

        Person.__post_init__(self)
        email2: str
        self.degree_type = randomFile.student_Degree()
        self.year_status = randomFile.student_year()
        self.college_hour_status = randomFile.student_status()
        self.current_credit_hours  = randomFile.student_credit_hours(self.college_hour_status)
        self.student_gpa_current = randomFile.student_gpa()
        self.student_full_name = self.person_full_name.replace(" ", "")
        email2 = self.email
        extension = email2.replace(self.student_full_name, "")
        found_college = randomFile.institution(extension)
        self.college = found_college

        # set graduation status
        self.total_credit_hours = randomFile.credits_completed(self.degree_type)
        self.graduation_student_status = randomFile.graduation_status(self.total_credit_hours, self.degree_type)

    def college_info(self) -> str:
         """
        display the academic information of the student object
        generated

                parameters:
                    self: instance of student object created

                return:
                    none
        """
        print("Institution: ", self.college)
        print("Degree: ", self.degree_type)
        print("Current GPA: ", self.student_gpa_current)
        print("Current Year: ", self.year_status)
        print("Status: ", self.college_hour_status)
        print("Current Credit Hours: ", self.current_credit_hours)
        print("Total College Credits: ", self.total_credit_hours)
        print("Graduation Status: ", self.graduation_student_status)


