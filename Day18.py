print("Hello Mitrooooo.....!")
print("Tar Ajj Apna Shiknar Ahota Decorators")

# ---------------------------------------- Part 1 --------------------------------------------------------------------------------
# Decorators
#           Decorator mhanje ek function jo dusrya function la modify karto, pan original function cha code change karat nahi.

# Real-life example:

# 🎁 Gift Box

# Gift = Original Function
# Gift Wrapper = Decorator

# Gift toch asto, pan wrapper mule to ajun attractive disato.

# Step 1: Function as Object
# Python madhye function la variable madhye store karu shakto.

# def greet():
#     print("Hello Dosatooo.....!")
# say_hello=greet
# say_hello()

# Function pan object aahe.

# Step 2: Function Inside Function

# def outer():
#     def inner():
#         print("Inside inner function");
#     inner()
# outer()


# Step 3: First Decorator

# def decorator(func):
#     def wrapper():
#         print("Before function")
#         func()
#         print("After Function")
#     return  wrapper

# @decorator
# def greet():
#     print("Hello Bhai....!")

# greet()


# @decorator mhanje kay?
# He:

# @decorator
# def greet():
#     print("Hello")

# He internally asa asto:

# def greet():
#     print("Hello")
# greet = decorator(greet)

# 🎯 Interview madhye ha question khup common aahe.

# ---------------------------------- Home Work Section ----------------------------------------------------------------------------

# Easy
# Decorator banva jo print karel:

# def decorator(display):
#     def wrap():
#         print("Start the Journy...!")
#         display()
#         print("End the Journy.....!")
#     return wrap

# @decorator
# def story():
#     print("Story of Journy....!")
# story()


# Medium

# Decorator banva jo function call honyapoorvi print karel:

# Function Started

# Ani nantar:

# Function Ended

# def decorator(add):
#     def calculator():
#         print("Functions Started.")
#         add()
#         print("Function Ended.")
#     return calculator

# @decorator
# def arthimatice():
#     n1=int(input("Enter the Number:-"))
#     n2=int(input("Enter the Number:-"))
#     print("The Sum of 2 number is ",n1+n2)

# arthimatice()
    


#-------------------------------------- Challenge ---------------------------------------------------

# Calculator function la decorator lava.
# Output:
# Calculation Started
# Answer 
# Calculation Finished


def decorator(calculator):
    def operation():
        print("Calculator are Started.")
        calculator()
        print("Calculator Finished...!")
    return operation

@decorator
def calculator():
    while True:
        print("......Menu......")
        print("1.Addition")
        print("2.subtaction")
        print("3.Multiplication")
        print("4.Division")
        print("5.MOdule")
        print("6.Exit")
        print("Choos the operation")
        chose =int(input("Choose inside in menu:- "))
        match chose:
            case 1:
                n1=int(input("Enter 1st number:- "))
                n2=int(input("Enter 2nd number:- "))
                print("Addition of two Numbers:- ",(n1+n2))

            case 2:
                n1=int(input("Enter 1st number:- "))
                n2=int(input("Enter 2nd number:- "))
                print("Subtaction of two Numbers:- ",(n1-n2))

            case 3:
                n1=int(input("Enter 1st number:- "))
                n2=int(input("Enter 2nd number:- "))
                print("Multiplication of two Numbers:- ",(n1*n2))

            case 4:
                n1=int(input("Enter 1st number:- "))
                n2=int(input("Enter 2nd number:- "))
                print("Division of two Numbers:- ",(n1/n2))


            case 5:
                n1=int(input("Enter 1st number:- "))
                n2=int(input("Enter 2nd number:- "))
                print("Module of two Numbers:- ",(n1%n2))

            case 6:
                print("Stop operations.....!")
                break;

            case _:
                print("Invali Choice...!")


calculator()

# -------------------------------------- Thank you --------------------------------------------------------------------------------
# print("Thanks Learn With me")