class Vehicle:
    def navigate(self):
        pass
class Car(Vehicle):
    def navigate(self):
        print("navigate via car")
class Truck(Vehicle):
    def navigate(self):
        print("navigate via truck")
Car().navigate()
Truck().navigate()
for v in [Car(), Truck()]:
    v.navigate()