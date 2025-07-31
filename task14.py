class User:
    def interact(self):
        pass

class Applicant(User):
    def interact(self):
        print("Ishga ariza topshirildi")

class Employer(User):
    def interact(self):
        print("Ish eloni joylandi")
applicant = Applicant()
applicant.interact()

employer = Employer()
employer.interact()
