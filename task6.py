class Employee:
    def calculate_bonus(self):
        pass

class Developer(Employee):
    def calculate_bonus(self):
        return "Developer bonusi: 10% oylikdan"

class Manager(Employee):
    def calculate_bonus(self):
        return "Manager bonusi: 20% oylikdan"
    
dev = Developer()
man = Manager()
print(dev.calculate_bonus())
print(man.calculate_bonus())
