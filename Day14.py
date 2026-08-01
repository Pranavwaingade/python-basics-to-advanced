print("Hello Mitrooooo.....!")
print("Tar Ajj Apna Shiknar Ahota Strings")

# ---------------------------------------- Part 1 -----------------------------------------------------
# Strings
#          String mhanje characters (letters, numbers, symbols) cha sequence.

name="Python"
# here Python is string

# 1. Indexing

# print(name[0])
# print(name[1])
# print(name[-1])


# 2. Slicing

# print(name[1:3])
# print(name[2:])
# print(name[:4])


# 3.String is Immutable

# name[0]="l"
# print(name)

# Write way 

# name= "l"+name[1:]
# print(name)


# 4. Length

# print(len(name))


# 5.Upper() & lower()

# print(name.upper())
# print(name.lower())


# 6.Strip()                 Extra spaces remove karto.

# text=" MERN StACK "
# print(text.strip())


# ---------------------------------- Home Work Section -------------------------------------------
# 1. "Python Developer" string create kara.
# 2. Length print kara.
# 3. Uppercase print kara.
# 4. Lowercase print kara.

# Str="Python Developer"
# print(len(Str))

# print(Str.lower())
# print(Str.upper())

# 1. " Hello Python " madhle spaces strip() ne remove kara.
# 2. Pahile 6 characters print kara.
# 3. Shevatche 5 characters print kara.

# Str2=" Hello Python "

# print(Str2.strip())

# print(Str2[:7])
# print(Str2[7:])


#-------------------------------------- Challenge ---------------------------------------------------

# User kadun nav ghya ani print kara:
# 1. Original Name
# 2. Uppercase
# 3. Lowercase
# 4. Length
# 5. First Character
# 6. Last Character


# name=input("Enter your name:- ")
# name=name.strip()
# print(name.upper())
# print(name.lower())
# print(len(name))
# print(name[0])
# print(name[-1])


# ---------------------------------------- Part 2 -----------------------------------------------------

# 1. replace()
# Ek word dusrya word ne replace karto.

# text="I LOVE JAVA"
# new_text=text.replace("JAVA","PYTHON")
# print(new_text)


# 2. split()
# String la list madhye convert karto.

# Str="Apple Banana Mango Chikuu"
# print(Str.split())


# 3. " ".join()
# List la string madhye convert karto.

# Fruits=["Apple","Banana","Mango","Chikuu"]
# print(" ".join(Fruits))


# 4.find()
# Substring kuthe aahe te sangto.

# Str1="I LOVE PYTHON"
# print(Str1.find("LOVE"))
# print(Str1.find("JAVA"))


# 5. startswith() & endswith()

# text="Python Developer"
# print(text.startswith("Python"))
# print(text.endswith("Developer"))

# 6. count()
# Word kiwa character kiti vela aahe.

# text="banana"
# print(text.count("a"))


# ---------------------------------- Home Work Section -------------------------------------------

# 1. "I Love Chikuu" madhye Java la Mango ne replace kara.
# text="I Love Chikuu"
# print(text.replace("Chikuu","Mango"))


# 2. "BMW Mustang Creata Fortuner" la split() kara.
# cars="BMW Mustang Creata Fortuner"
# print(cars.split())

# List:  join() vaprun sentence banva.

# Str=["Python", "is", "Awesome"]
# print(" ".join(Str))

# "Programming" madhye "gram" cha index find() ne shodha.

# txt="Programming"
# print(txt.find("gram"))


# User kadun ek sentence ghya ani print kara:

# Total Length
# Number of words (split())
# Uppercase
# Lowercase
# "Python" aahe ka? (find())

# Sentense=input("Enter the Sentense:- ")

# print(len(Sentense))
# print(len(Sentense.split()))
# print(Sentense.upper())
# print(Sentense.lower())
# print(Sentense.find("Python"))


# -------------------------------------- Thank you ---------------------------------------------------
# print("Thanks Learn With me")
