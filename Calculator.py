# Calculator using oop

class calculator():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self,x,y):
        print('sum:', x+y)
    def subtraction(self,x,y):
        print('subtraction:',x-y)
    def multiply(self,x,y):
        print('Multiplication:',x*y)
    def Division(self,x,y):
        print('Division:',x/y)
       



x=int(input('Enter the value of x:'))
y=int(input('Enter the value of y:'))


c1=calculator(x,y)
c1.add(x,y)
c1.subtraction(x,y)
c1.multiply(x,y)
c1.Division(x,y)
print(c1)