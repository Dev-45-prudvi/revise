from math import *
from myclass import Student
from inheritance import Student1
print("Hi,I am Prudvi")

#variables and datat_types
age=22
print(age)
name="Prudvi"
print(name)
isMale=True

#working with strings
print("Hi,I am \"Prudvi\"\nAnd I am 22 years old")
print("Hi I am " +name+ " And I am "+str(age)+" years old")
print(name.lower())
print(name.upper())
name=name.upper()#changed name variable to uppercase.
print(name.isupper())
print(name.lower().islower())#chaining Function
print(len(name))
name=name.replace("PRUDVI","VENKAT")#changed name to VENKAT
print(name)
print(name.index("V"))

#working with numbers
print(abs(age))
print(pow(age,2))
print(max(age,34,48))
print(min(age,34,48))
print(round(2.56))
print(ceil(2.56))#used math library to use this functions.
print(floor(2.56))
print(round(sqrt(age)))

#input from the user
"""
name1=input("Enter your name: ")
print(name1)
print(name)
num=int(input("enter a number: "))#by default input from user taken as string u need to convert it to integer.
print(num+22)
"""

#Lists
family=["Murali","Padmaja","Prudvi","Satvika"]
ages=[47,38,22,20]
print(family)
print(ages)
family.extend(ages)
print(family)
family.append("Mohan")
print(family)
family.insert(2,"Penumarthi")
print(family)
family.remove("Penumarthi")
print(family)
family.pop()
print(family)
ages.sort()
print(ages)
family.reverse()
print(family)
familycopy=family.copy()
print(familycopy)
family.clear()
print(family)

#Tuples:Immutable.
fruits=("Apple","mango","banana")
print(fruits)
print(len(fruits))
print(fruits[0])

#Functions
def greeting(name):
    print("Hi,I am "+name)
    return "sucessfully greeted"#used to get information back from function
    print("Hello World!")#will not be executed after return statement.
print(greeting("dev"))

#If Statements
eligible_age=int(input("Enter your age: "))
if eligible_age>=60:
    print("You are eligible for pension")
elif eligible_age<60:
    print("You are not eligible for pension")
else:
    print("Enter valid age")

#Dictionaries
combine={
    "Murali":47,
    "Padmaja":38,
    "Prudvi":22,
    "Satvika":20
}
print(combine)
print(combine["Murali"])
print(combine.get("Murali"))

#whileloop
multiplicand=int(input("Enter your multiplicand: "))
"""
i=0
while i<=20:
    print(multiplicand*i)
    i+=1
"""


#forloop
for i in range(20):
    print(multiplicand*i)

#Exponent funtion
def expo(base,exponent):
    result=1
    for index in range(exponent):
        result=result*base
    return result

print(expo(2,3))

#2Dlists and Nested Loops
genz=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(genz)
print(genz[0][2])#row number,column number
for row in genz:#nested Loops
    for cols in row:
        print(cols)

#TRY AND EXCEPT
try:
    num=int(input("enter a number: "))
    print((str(num)+" years old"))
except:
    print("enter a valid number")

#ReadingFiles
file=open("requirement.txt","r")
new_file=open("readme.md","w")#created new file.
#file.write("I am 22 Years old")
print(file.readable())
print(file.readline())
file.close()
new_file.close()


#Classes And Objects
student1=Student("prudvi",22,99220040334,"CSE",False)#Object Creation.
print(student1.name)
student2=Student1("nandu",22,99220040313,"CSE",False,8.4)
print(student2.name)
print(student2.cgpa)















