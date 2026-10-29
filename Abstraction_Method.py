from abc import ABC, abstractmethod # Abstraction till python 2.0 to continue

class PaymentProcessor(ABC): 
    @abstractmethod # Annotation For Method
    def process_payment(self, ammount):
        print("Payment Process.")
    def print_Recipt(self, ammount):
        print("Recipt Printed. ")
    
class CreditcardPayment(PaymentProcessor):
    def process_payment(self, ammount):
        print("Deducting From your Credit card.")

class UPIPayment(PaymentProcessor):
    def process_payment(self, ammount):
        print("Payment Success in UPI.")

def checkout(processor, ammount):
    processor.process_payment(ammount)
    processor.print_Recipt(ammount)

cpayment = CreditcardPayment()
checkout(cpayment, 100)

upayment = UPIPayment()
checkout(upayment, 200)