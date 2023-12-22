'''import module1
module1.fun()'''

'''from module1 import *
fun()'''


'''from calculator import*
cal()'''


from calculator import *

num1 = float(input("Enter 1st choice:"))
num2 = float(input("Enter 2nd choice:"))             
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
n = int(input("Enter your choice:"))
if n==1:
    print(addition(num1,num2))
elif n==2:
    print(sub(num1,num2))
elif n==3:
    print(multiplication(num1,num2))
else:
    print("wrong input !\n please Enter a proper number")
    
        
        







             
