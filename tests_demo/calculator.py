# request first number
#num1 = int(input("insert first number: "))

# request second number
#num2 = int(input("insert second number: "))

# output total
#num3 = num1 + num2

#print(num3)

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def get_sum(self):
        return self.a + self.b
    
    def get_difference(self):
        return self.a - self.b
    
    def get_product(self): 
        return self.a * self.b   
    
    def get_quotient(self): 
        if self.b == 0:
            raise ValueError('cannot divide by 0.')
        return self.a / self.b  
    
if __name__ == '__main__':
    x = Calculator(a=10, b=5)
    answer = x.get_quotient()
    print(answer)