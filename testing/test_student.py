'''
test the student classes to see what happeneds 
'''
import student as st
from dataclasses import dataclass, field


# class to test out the person class
class Test_Person:
    def test_details(self):
        s = st.Person()
        print("Testing details: Person Class")
        assert type(s.first_name) == str
        assert type(s.last_name) == str
        assert type(s.person_full_name) == str
        assert type(s.email) == str
        assert type(s.student_id) == int
        assert type(s.student_phone_number) == str
        assert type(s.student_ssid) == str
        assert type(s.student_address) == str
    
    def test_setting_details(self):
        test_person = st.Person()
        test_person.person_full_name = "Terry Jones"
        test_person.first_name = "Terry"
        test_person.last_name = "Jones"
        test_person.email = "TerryJones@harper.edu"
        test_person.student_id = 123456
        test_person.student_phone_number = "777-777-7777"
        test_person.student_id = "892-87-3695"
        test_person.student_address = "8566 Yeater Lane"

    def test_person(self):
        single = st.Person("Jenny")

    def test_methods(self):
        single_person = st.Person()
        single_person.person_info("Dont accept")

class Test_Student:
    def test_details_student(self):
        s = st.Student()
        print("Testing details: Student Class")
        assert type(s.college) == str
        assert type(s.degree_type) == str
        assert type(s.year_status) == str
        assert type(s.college_hour_status) == str
        assert type(s.current_credit_hours) == int
        assert type(s.total_credit_hours) == int
        assert type(s.student_gpa_current) == float
        assert type(s.graduation_student_status) == bool
        assert type(s.student_full_name) == str

    def test_setting_details2(self):
        test_person2 = st.Student()
        test_person2.college = "Yeat Univeristy"
        test_person2.degree_type = "Associate"
        test_person2.year_status = "Freshman"
        test_person2.college_hour_status = "Part time"
        test_person2.current_credit_hours = 6
        test_person2.total_credit_hours = 35
        test_person2.student_gpa_current = 3.12
        test_person2.graduation_student_status = False 
        test_person2.student_full_name = "Hugh Janus"

    def test_student(self):
        student = st.Student(1234)

    def test_methods(self):
        student = st.Student()
        student.college_info("Yeet")
