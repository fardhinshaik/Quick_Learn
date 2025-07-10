from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class UPI(PaymentMethod):
    def pay(self, amount):
        print(amount)
a = UPI()
a.pay(100)
