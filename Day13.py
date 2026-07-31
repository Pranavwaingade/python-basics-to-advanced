print("Hello Mitrooooo.....!")
print("Tar Ajj Apna Shiknar Ahota Sets")

# ---------------------------------------- Part 1 -----------------------------------------------------
# Sets
#      Set ha ek collection data type aahe jo: 1. Duplicate values allow karat nahi.
#                                              2. Unordered asto (order fix nasto).
#                                              3. Mutable aahe (add/remove karta yeto).


# Example 1

# fruits={"Apple","Mango","Banana","Chikuu"}
# print(fruits)


#Example 2     How to create sets

# numbers={10,20,30,40,50}
# print(numbers)


# Example 3  HOw to add element

# numbers.add(60)
# print(numbers)



# Example 4 How to remove element

# numbers.remove(50)
# print(numbers)

# numbers.remove(90)
# print(numbers)

# | ------------------------------------------------|
# |   remove() → Element nasel tar KeyError.        |
# |   discard() → Element nasel tari error nahi.    |
# | ------------------------------------------------|

# Example 5  Used discard

# numbers.discard(90)
# print(numbers)


# -----------------------------------------------------------------------------------------------------------

# List vs Tuple vs Set
# | Feature    | List   | Tuple  | Set  |
# | ---------- | -----  | -----  | -----|
# | Ordered    | ✅    | ✅     | ❌   |
# | Mutable    | ✅    | ❌     | ✅   |
# | Duplicates | ✅    | ✅     | ❌   |
# | Indexing   | ✅    | ✅     | ❌   |


# ---------------------------------- Home Work Section -------------------------------------------
 
# 1. 5 fruits cha set banva.
# 2. Ek fruit add() kara.
# 3. Ek fruit remove() kara.

# fruits={"Apple","Oranage","Mango","Banana","Kiwi"}
# print(fruits)

# fruits.add("Chikuu")
# print(fruits)

# fruits.remove("Kiwi")
# print(fruits)

# discard() vaprun naslela element remove karun bagha.

# fruits.discard("Watermelon")
# print(fruits)


# Example 
# numbers = {10, 20, 20, 30, 40, 40, 50}
# 1. Output kay yeil?
# 2. Ka yeil?
# 3. 60 add kara.
# 4. 10 remove kara.

# Answer:- 

# numbers = {10, 20, 20, 30, 40, 40, 50}
# 1.print kalya var numbers print hotila sets madhea pan without any sequence ani 20,40 yeakda cha print honara Dubplicate not allowed 
# 2. karna ki Sets hea unorderd asata taa ,ani dublicate allowed nasata 
# print(numbers)

# numbers.add(60)
# print(numbers)

# numbers.remove(10)
# print(numbers)


# ---------------------------------------- Part 2 -----------------------------------------------------
# 1. Union ( | and union() )
#  don Sets madhela saglea unique elemnts ekatra yeata

# set1={1,2,3,4,5,6,7}
# set2={6,7,8,9,10,11}

# print(set1.union(set2))
# print(set1 | set2 )


# 2. Intersection ( & and intersction())
#  Don Sets madhlea Common Print hota taa 

# print(set1.intersection(set2))
# print(set1 & set2)


# 3.Differnce( - and differnce() )
# joo first set ahea tya madhala dusraya set madhea nahi tea print karya cha

# print( set1 - set2 )
# print(set2.difference(set1))


# 4.Symetric differnce ( ^ )
# jea common soduna sagal print honara

# print(set1 ^ set2)


# 5.MemberShip Operator
# help karata element tya set madhi ahea ki nahi olakahay laaa

# print(10 in set2)
# print(12 in set2)


# ---------------------------------- Home Work Section -------------------------------------------
# 1. Union print kara.
# 2. Intersection print kara.
# 3. Difference print kara.
# 4. Symmetric Difference print kara.

# A = {10, 20, 30}
# B = {30, 40, 50}
# print( A | B)
# print( A & B)
# print( A - B)
# print( A ^ B)



#-------------------------------------- Challenge ---------------------------------------------------


# Create 2 sets:

# students_java = {"Pranav", "Rahul", "Amit"}
# students_python = {"Pranav", "Rohit", "Amit"}

# Print:
# Common students
# Only Java students
# All students
# Only one language shiklele students

# print(students_java & students_python)
# print(students_java - students_python)
# print(students_java | students_python)
# print(students_java ^ students_python)


# -------------------------------------- Thank you ---------------------------------------------------
# print("Thanks Learn With me")
