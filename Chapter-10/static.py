class Calculator:
    def __init__(self,number):
        self.number = number
    
    def square(self):
        print(f"square of {self.number} is: {self.number ** 2}")

    def cube(self):
        print(f"cube of {self.number} is: {self.number ** 3}")

    def squareroot(self):
        print(f"square root of {self.number} is: {self.number ** 0.5}")

    @staticmethod
    def greet():
        print("Hello!!, Congratulations, you have written your program")

c = Calculator(4)
c.cube()
c.square()
c.squareroot()
c.greet()