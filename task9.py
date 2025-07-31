class Notification:
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        print(" Email yuborildi")

class SMSNotification(Notification):
    def send(self):
        print(" SMS yuborildi")
email = EmailNotification()
email.send()

sms =SMSNotification()
sms.send()
