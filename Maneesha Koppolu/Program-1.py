class caliculator:
    def __init__(self,a,b,operation):
        self.a=a
        self.b=b
        self.operation=operation.lower()
    def caliculation(self):
        if self.operation=="add":
            return self.a + self.b
        elif self.operation =="sub":
            return self.a - self.b
        elif self.operation=="mul":
            return self.a * self.b
        elif self.operation=="div":
            if self.b==0:
                return "Error: Division by zero is not allowed"
            return self.a / self.b
        else:
            return "Invalid type"
        
a=float(input("Enter the a value :"))
b=float(input("Enter the b value :"))
operation=input("Enter the opearation you like to perform :")
cal=caliculator(a,b,operation)
result=cal.caliculation()
print("Result",result)
