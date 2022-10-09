class Calculator:

    @staticmethod
    def greet():
        print("\n****************WELCOME****************")

    def __init__(self, num):
        self.number= num
    
    def square(self):
        print(f"The square of {self.number} is {self.number **2}")

    def squareroot(self):
       print(f"The squareroot of {self.number} is {self.number **0.5}")

    def cube(self):
       print(f"The cube of {self.number} is {self.number **3}")
    
a= Calculator(9)
a.greet()
a.square()
a.squareroot()
a.cube()