students=[]
grades=[]
while True:
   student =str(input("Please give me the name of the student: "))
   if student =="l":
       for i in range(students, grades):
           print ("Student: " + i[0] + " Grade: " + i[1])
       break
   grade =input("Please give me their grade: ")
   students.append(student)
   grades.append(grade)
list1=["orange","strw"]
thisset={"apple","banana","cherry"}
print(thisset)
thisset.update(list1)
print(thisset)
z=int(input("how many element you want to remove:"))
for i in range(z):
    thisset.pop()
    print(thisset)
m=input("you want to remove or clear the set:")
if (m=="remove"):
    (thisset.remove())
else:
    (thisset.clear())
print(thisset)
4
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))
#3
def reverse_string(str):  
    str1 = ""  
    for i in str:  
        str1 = i + str1  
    return str1    
     
str =input("enter:")     
print("The original string is: ",str)  
print("The reverse string is",reverse_string(str))
#2
lst =[]
num =int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number:'))
    lst.append(numbers)
print("Sum of elements in given list is :", sum(lst))
#1
def maximum(a,b,c):
	if (a >= b) and (a >= c):
		largest = a
	elif (b >= a) and (b >= c):
		largest = b
	else:
		largest = c
	return largest
a =input("the first number is:")
b =input("the second number is:")
c =input("the therd number is:")
print(("the max of three number is"),maximum(a, b, c))

# Program make a simple calculator

# This function adds two numbers
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

print("Select operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")


l1=[1426,6636,858458,986989,235213,8654,4525515671542333]

[print("odd :",i) if i%2!=0 else print("even:",i) for i in l1]
l2=[]

dict1={2002:"brazil",2006:"italy",2010:"spain",2014:"germany",2018:"france"}
del dict1[2002]
print(dict1)

birthdays={}
ans="y"
while ans=="y":
    name=input("enter a name:")
    bday=input("enter s birthday:")
    if name not in birthdays:
        birthdays[name]=bday
    else:
        print("that entry aleredy exists")
    print("\nthe birthday divt contain:",birthdays)
    ans=input("\nadd another entry?(y for yes)")
print("\nname\t\t birthdays")
print("-----------------------------------------")
for name in birthdays:
    print(name,"\t\t",birthdays[name])
farm={"cats":10,"dogs":7,"cows":5,"horses":1}
print(farm["cats"])#1
print(farm.keys())#2
print("hen"in farm)#3
farm["dogs"]=farm["dogs"]+2#4
print(farm)
farm["rabbit"]=1#5
print(farm)
del farm["horses"]#6
m1=max(farm.values())
for x in farm:
    if farm[x]==m1:
       print("the element that is the most existing",x)


partc=[{'first':'tom','last':'white','age':'35'},{'first':'ted','last':'smith','age':'21'},{'first':'sarah','last':'lewis','age':'40'}]
for partci in partc:
    print(partci['first'],"\t",partci['last'],"\t",partci['age'])
a={"lenovo","hp","del","accent","asus"}
b={"acer","thomson"}
def union1():
    for i  in a:
        b.add(i)
    return(b)
print(union1())
