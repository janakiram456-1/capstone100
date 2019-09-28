def add(x, y):
   return x + y
# This function subtracts two numbers
def subtract(x, y):
   return x - y
# This function multiplies two numbers
def multiply(x, y):
   return x * y
# This function divides two numbers
def divide(x, y):
   return x / y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
# Take input from the user
choice = input("Enter choice(+ | - | / | x):")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
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

