class Marks:
    def __init__(self):
        self.__math = 0
    def display(self):
        print(self.__math)
    def update_marks(self, math):
        self.__math += math
det = Marks()
det.display()
det.update_marks(100)
det.display()