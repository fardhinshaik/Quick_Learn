class User:
    def login(self):
        print("Logging in")
    def logout(self):
        print("Logging out")
class Business:
    def add_stocks(self):
        print("Taking you to the stocks management.")
    def buy_stocks(self):
        print("Buying stocks")
class Use(Business, User):
    def sell_stocks(self):
        print("Selling stocks")
    def manage_stocks(self):
        print("Manage stocks")
u1 = Use()
u1.login()
u1.add_stocks()
u1.buy_stocks()
u1.manage_stocks()
u1.sell_stocks()
u1.logout()