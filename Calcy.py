def add(x, y):
   return x + y

def divide(x, y):
   return x / y
# This function subtracts two numbers
if choice == '+':
   print(num1,"+",num2,"=", add(num1,num2))
elif choice == '-':
   print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == 'x':
   print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '/':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")
