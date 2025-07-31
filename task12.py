class User:
    def get_dashboard(self):
        pass

class Student(User):
    def get_dashboard(self):
        print("Dashboard: Kurslar royxati, vazifalar")

class Instructor(User):
    def get_dashboard(self):
        print("Dashboard: Kurs statistikasi, topshiriqlar tahlili")

student = Student()
student.get_dashboard()

instructor = Instructor()
instructor.get_dashboard()