class User:
    def __init__(self, username):
        self.username = username

    def access_level(self):
        pass

class Admin(User):
    def access_level(self):
        return f"{self.username}: Full access (read, write, delete)"

class Guest(User):
    def access_level(self):
        return f"{self.username}: Limited access (read only)"

admin_user = Admin("admin")
guest_user = Guest("mehmon1")

print(admin_user.access_level())
print(guest_user.access_level())
