#import random
#s=random.randint(1,100)
#i=0
#while(i<5):
  #numb=int (input("give a number between 1 and 100"))
  #if numb<s:
      #  print("your number is less")
       
  #elif numb>s:
        #print("your number is greater")
  #elif numb==s:
        #print("you win")
        #break
#else:
    #print("you lose") 
"""i=0
a=0
while(i<5):
    nb=int (input("the number is "))
    if(nb>=0):
        a=a+1
    i=i+1
print("the positive number ",a)"""
    

"""nb=int(input("how much the number of the employees: "))
print("enter their name birthday and their salary if it is exist: ")
name = list()
birth=list()
salary=list()
c=0
while c<nb:
    name.append(input("enter your name: "))
    birth.append(input("enter your birth: "))
    salary.append(input("enter your salary: "))
    c=c+1
c=0
print("name","\t","birhtday","\t","salary")
while c<nb:
    print(name[c],"\t",birth[c],"\t","\t",salary[c])
    c=c+1"""
max=0
i=0
while i<3:
    nb = int(input("enter a nb:"))
    if max<nb:
        max=nb
        i=i+1  
print(max)