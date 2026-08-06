print("Hello Mitrooooo.....!")
print("Tar Ajj Apna Shiknar Ahota Lambda Functions")

# ---------------------------------------- Part 1 --------------------------------------------------------------------------------
# Lambda Functions
#                  Lambda function ha anonymous function aahe. (Anonymous mhanje tyala nav (name) nasto.)

# Normal Function 

# def add(a , b):
#     return a+b
# print(add(10 ,20))

# Lambad Function 

# add = lambda a,b:a+b
# print(add(10,20))

# Syntax  lambda argument : expression 

# square = lambda x:x*x
# print(square(5))


# multiple argument and sorting also

# students=[("Pranav",90),("Bhaktuu",95),("Ram",80)]
# students.sort(key=lambda x : x[0])
# print("Alaphabeaticaly Sort:- ",students)
# students.sort(key=lambda x : x[1])
# print("MArks wise sort:- ",students)


# ---------------------------------- Home Work Section ----------------------------------------------------------------------------

# Easy 

# 7 cha square print kara.
# square = lambda x: x*x
# print(square(7))

# add = lambda a,b:a+b
# print(add(10,25))

# sorted() vaprun ascending order madhye print kara.
# number=[5,2,8,1]
# number.sort()
# print("Sorted array :- ",number)


# Largest number shodhnara lambda function banva.
# largest = lambda a,b : a if a > b else b
# number1=int(input("Enter the 1st number:- "))
# number2=int(input("Enter the 2nd number:- "))
# print("Largest number is:- ",largest(number1,number2))


# Lambda vaprun marks descending order madhye sort kara.
# students = [
#     ("Pranav", 85),
#     ("Rahul", 70),
#     ("Amit", 95),
#     ("Rohit", 80)
# ]
# students.sort(key=lambda x : x[1])
# print(students)

#-------------------------------------- Challenge ---------------------------------------------------

# products = [
#     ("Laptop", 50000),
#     ("Mouse", 700),
#     ("Keyboard", 1500)
# ]

# sort=sorted(products, key=lambda x:x[1])
# condtion= [i for i in sort if i[1] > 1500]
# print(condtion)


# -------------------------------------- Thank you --------------------------------------------------------------------------------
# print("Thanks Learn With me")