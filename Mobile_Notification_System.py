from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, recipient, message):
        pass

    def log_delivery(self, recipient):
        print(f"\t> Notification Successfully Send to: {recipient}.\n")
    
class Sms_Notification(Notification):
    def send(self, recipient, message):
        print(f"Connecting to SMS Server....\n\t> Sending SMS to {recipient}\t| > Message: '{message}'")

class Email_Notificaction(Notification):
    def send(self, recipient, message):
        print(f"Connecting to E-Mail Server....\n\t> Sending E-Mail to {recipient}\t| > Message: '{message}'")
    
def Accepts_Notificatoins(Notification_obj, User, text):
    Notification_obj.send(User, text)
    Notification_obj.log_delivery(User)

sn = Sms_Notification()
Accepts_Notificatoins(sn, 'Rahul', "Hi bro, What's up?")

en = Email_Notificaction()
Accepts_Notificatoins(en, 'Tony', "Hello Sir,  I am JARVIS.")
