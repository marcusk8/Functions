# Funcctions - a block instructions to d an actions. They're used to organize code.

# 2 thing required to do:
# 1 define the function 
#2 call the function

# define the function
# def greeting():
# print("Hello!")

# call function
# greeting()

# # function with parameter, a parameter is a value to plug into a function, for the function to use in creating an output
# def greeting(name):
#   print("Hello! " + name)

# guest name = input("What is your name: ")
# # call function
# greeting(guestname)

def addNumbers(num1, num2):
  print(num1 + num2)

def subNumbers(num1, num2):
  print(num1 - num2)

  
  
# addNumbers(2,3)

# ask user to enter 2 numbers. Plug these two numbers into the addNumberss function

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
operator = input("Add or Subtract: ")


if operator.lower() == "add":
  addNumbers(num1, num2)
elif operator.lower() == "subtract":
  subNumbers(num1, num2)
else:
  print("That's an invalid name.")
