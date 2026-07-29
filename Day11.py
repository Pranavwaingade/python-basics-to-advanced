print("Hello Mitrooooo.....!")
print("Tar Ajj Apna Shiknar Ahota Exception Handling")

# -----------------------------------------------------------------------------------------------
# Exception Handling
#                    Exception Handling mule program error alyavar band padat nahi.

# Example 1

# try:
#     num1=int(input("Enter The First Number:- "))
#     num2=int(input("Enter The Second Number:- "))
#     print("The Division is ",num1/num2)
# except ZeroDivisionError:
#     print("Number Cannot be divide zero")

# Example 2

# try:
#     num = int(input("Enter a number"))
#     print(10/num)

# except ValueError:
#     print("Enter a Valid a Number")

# except ZeroDivisionError:
#     print("Number Cannot be Divide Zero")



# ---------------------------------- Home Work Section -------------------------------------------

# 1. User kadun 2 numbers ghya ani division kara.
# Jar second number 0 asel tar: Cannot divide by zero.

# try:
#     num1=int(input("Enter The Number:- "))
#     num2=int(input("Enter The Number:- "))
#     print("Division is ",num1/num2)        

# except ZeroDivisionError:
#     print("Number Cannot be Divide Zero")


# 2. User kadun number ghya.
# Jar user "abc" sarkha text takel tar:

# try:
#     num1=int(input("Enter The Number:- "))
#     num2=int(input("Enter The Number:- "))
#     print("Division is ",num1/num2)        

# except ValueError:
#     print("Invalid Input")

#-------------------------------------- Challenge ---------------------------------------------------

# Calculator banva: Add Subtract Multiply Divide
# Saglya operations try-except madhye handle kara. Program crash hou deu naka.

# def calculator(operaction):
#         if operaction == "Add":
#             try:
#                 num1=int(input("Enter the 1st Number:- "))
#                 num2=int(input("Enter the 2nd Number:- "))
#                 print("Addition is:-",num1+num2)
#             except ValueError:
#                 print("Invalid Input")
        
#         elif operaction == "Sub":
#             try:
#                 num1=int(input("Enter the 1st Number:- "))
#                 num2=int(input("Enter the 2nd Number:- "))
#                 print("Subtraction is:-",num1-num2)

#             except ValueError:
#                 print("Invalid Input")
        
#         elif operaction == "Pro":
#             try:
#                 num1=int(input("Enter the 1st Number:- "))
#                 num2=int(input("Enter the 2nd Number:- "))
#                 print("Product is:-",num1*num2)

#             except ValueError:
#                 print("Invalid Input")

#         else:
#             try:
#                 num1=int(input("Enter the 1st Number:- "))
#                 num2=int(input("Enter the 2nd Number:- "))
#                 print("Dividion is:-",num1/num2)

#             except ValueError:  
#                 print("Invalid Input")


# operaction=str(input("Enter The Operation(Add ,Sub ,Pro ,Div):- "))
# calculator(operaction)
    
# -------------------------------------- Thank you ---------------------------------------------------

# print("Thanks Learn With me")