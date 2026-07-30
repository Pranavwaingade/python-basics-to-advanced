print("Hello Mitrooooo.....!")
print("Tar Ajj Apna Shiknar Ahota Tuples")

# ---------------------------------------- Part 1 -----------------------------------------------------
# Tuples
#      Tuple ha Python madhla collection data type aahe. To ekach variable madhye multiple values store karto.

# Example 1

# fruits=("Apple","Banana","Mango")
# print(fruits)


# This is List

# car=["BMW","Mustang","Nexon"]
# car[0]="Lamborghini"
# print(car)


# This is Tuple 

# car=("BMW","Mustang","Nexon")
# car[0]="Lamborghini"
# print(car)


# Tuple is Immutable.
# Major Diffence between list or tuple is list can change the data but tuple is not 
# -----------------------------------------------------------------------------------------------------------
# Tuple Create Karnyache Ways
# Method 1

# t=(1,2,3)
# print(type(t))

# Method 2
# Python automatically tuple banvto.

# t=1,2,3
# print(type(t))

# Method 3
# List pasun tuple create karto.

# t=tuple([1,2,3,4])
# print(type(t))

# Method 4
# Jara single vlaue aslea tar

# t=10,
# print(type(t))

# ---------------------------------- Home Work Section -------------------------------------------
# 1. 5 colors cha tuple banva.
# 2. Type check kara using type().
# 3. Single-element tuple create kara.
# 4. List la tuple madhye convert kara.

# Colours=("Red","Green","Blue","Yellow","Black")
# print(Colours)
# print(type(Colours))

# colour=("Red",)
# print(type(colour))

# colour_list=["Red","Green","Blue","Yellow","Black"]
# colour_tuple=tuple(colour_list)
# print(colour_tuple)


# ---------------------------------------- Part 2 -----------------------------------------------------
# 1. Indexing
# Tuple madhla pratyek element la index asto.
# fruits=("Apple","Banana","Mango","Orange")
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# print(fruits[3])


# 2. Negative Indexing
# Python madhye ulat side ne pan access karta yeta.
# print(fruits[-1])
# print(fruits[-2])


# 3. Slicing
# Tuple madhun kahi elements kadhayche astil tar slicing vaparto.

# number=1,2,3,4,5,6,7,8,9,10

# print(number[:8])
# print(number[1:4])
# print(number[5:])


# 4.Packing
# Multiple values ek tuple madhye store karne.

# student=("Pranav",21,"Pune")
# print(student)

# 5.Unpacking

# student=("Pranav",21,"Pune")
# name,age,city=student
# print(name)
# print(age)
# print(city)

# 6. count()    Ek value kiti vela aali te sangto.

# num=1,2,3,2,4,5,2,6,2,7,2,8,2,9,2
# print(num.count(2))

# 7. index()        Value kontya position la aahe te sangto.

# num=1,2,3,4,5,6,7,8,9,10
# print(num.index(5))

# ---------------------------------- Home Work Section -------------------------------------------

# 1. 5 subjects cha tuple banva.
# 2. 3rd subject print kara.
# 3. Last subject print kara.
# 4. Slicing vaprun pahile 3 subjects print kara.
# 5. Shevatche 2 subjects print kara.

# Subjects=("Maths","Ds","Web technology","TCS","Data Science")
# print(Subjects[2])
# print(Subjects[-1])

# print(Subjects[:3])

# print(Subjects[3:])


# 6.
# Cars=("BMW" ,"M8",280000000)
# Brand ,Model ,Price =Cars
# print("Car Brand:- ",Brand)
# print("Car Model:- ",Model)
# print("Car Price:- ",Price)


#-------------------------------------- Challenge ---------------------------------------------------

# numbers = (10, 20, 10, 30, 40, 10, 50)
# 10 kiti vela aahe?
# 30 cha index kay aahe?
# Last 4 elements slice kara.

# numbers=(10, 20, 10, 30, 40, 10, 50)
# print(numbers.count(10))
# print(numbers.index(30))
# print(numbers[3:])
    
# -------------------------------------- Thank you ---------------------------------------------------

# print("Thanks Learn With me")
