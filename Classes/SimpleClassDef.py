class Programmer:
    
    company="Microsoft"
    def __init__(self, name, product):
        self.name= name
        self.product= name
    
    def disp(self):
        print(f"The name of the {self.company} programmer is {self.name} and the product is {self.product}")
bilal= Programmer("Bilal", "Forza")
john= Programmer("John", "Skype")
bilal.disp()
john.disp()