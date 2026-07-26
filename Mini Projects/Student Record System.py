
students=[]
student={}
name=input("Enter Your Name:- ")
age=int(input("Enter Your Age:- "))
city=input("Enter City Name:- ")
course=(input("Enter Course Name:- "))

student["name"]=name
student["age"]=age
student["city"]=city
student["course"]=course


students.append(student)



for student in students:
    print("\n-------- Student Record ---------")
    print("Name:-",student["name"])
    print("Age:-    ",student["age"])
    print("City:-   ",student["city"])
    print("Course:- ",student["course"])

