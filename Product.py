class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def display(self):
        print(f"The Price of the {self.name} product is now ${self.price}.")
p1 = Product("Whey Protien", 3000)
p2= Product("Protien Bars", 1000)
p1.display()
p2.display()