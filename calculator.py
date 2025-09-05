"""
TASK: Create a Calculator class.

Requirements:
1. The class should allow basic operations: add, subtract, multiply, divide.
2. Each operation should be a separate method.
3. Handle division by zero gracefully.
4. Allow both integers and floats.

Example Usage:
    calc = Calculator()
    print(calc.add(5, 3))        # 8
    print(calc.divide(10, 0))    # "Error: Division by zero"
"""
try:
    class Calculator:
        def __init__(self,a,b):
            self.a = a
            self.b = b
        def add(self,a,b):
            return a+b
        def sub(self,a,b):
            return a-b
        def div(self,a,b):
            return a/b
        def mult(self,a,b):
            return a*b
        def exp(self,a,b):
            return a**b
    calculator = Calculator(2,3)
    print(calculator.div(21,10))
    
    
except ZeroDivisionError:
    print('Error Division by 0')
