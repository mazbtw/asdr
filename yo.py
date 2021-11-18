
#students=["mhmd","hassan","ahmad","ali"]
#grades=[18,16,15,14]
#for i in range(len(students)):
  #  print(students[i],"\t",grades[i])
#names1=[]
#nb_cars=int(input("enter the nb of cars:"))
#for i in range(nb_cars):
    #car_name=input("enter name of cars:")
    #if car_name not in names1:
        #names1.append(car_name)
#print(names1)
#for i in range(len(names1)):
#    # print(names1[i],end="_")
# fruits=['banana','apple','adjn']
# newlist=[x if x !="banana" else "orange"for x in fruits]
# print(newlist)
# newlist2=["hello"for x in fruits]
# print(newlist2)

# x=[1,2,3,4,5,]
# y=[10,9,8,7,5]
# sumlist=[]
# print("first list is:",x)
# print("the second list is:",y)
# for i in range(len(x)):
#     sum=x[i]+y[-i-1]
#     sumlist.append(sum)
# print(sumlist)
# n=input("enter a nb: ")
# names=[]
# cap_names=[]
# for i in range(int(n)):
#   print("enter name",i+1,": ")
#   name=input()
#   names.append(name)
# for i in range(int(n)):
#   cap_names[i]=names[i].capitalize
# print (cap_names)
# list1=[]
# mylist=[76,92.3,"hello",True,4,76]
# mylist.append("apple")
# print(mylist)
# mylist.append(76)#a9t8
# print(mylist)
# mylist.insert(2,"cat")#b
# print(mylist)
# mylist.insert(0,"99")#c
# print(mylist)
# mylist.count(76)#e
# print(mylist)

# mylist.remove(76)#f
# print(mylist)
# its remix coming with bow bow bow, eren yeagar, like baka,
# N=int(input("Enter nb: "))
# list1=[]
# list2=[]
# for i in range(N):
#   name=str(input("enter name"+str(i+1)+":"))
#   list1.append(name)
# for x in list1:
#   if  x not in list2:
#     list2.append(x)
# print("after removing",list2)
# import random
# i=0
# x=[]
# for i<100:
#   x=random.randint(0,100)
#   i=i+1
#   print(x)
# import random
# l=[]
# max=0
# min=0
# sum=0
# for i in range (0,10):
#   x=random.randint(1,10)
#   l.append(x)
# for i in range (0,10):
#   if max<l[i]:
#     max=l[i]
# for i in range (0,10):
#   if min>l[i]:
#     min=l[i]
# for i in range(0,10):
#   sum=sum+l[i]
# av=sum/len(l)
# print(l)
# print(min)
# print(av)
# print(max)
# def hey(name1,name2,name3):
#   print("welcome",name1)
#   print("welcome",name2)
#   print("welcome",name3)
# a=input("enter the first name")
# c=input("enter the second name")
# b=input("enter the therd name")
# hey(a,b,c)
# N=int(input("enter nb: "))
# def hey():
#    print("welcome",a,"nice to meet you")
# for i in range(N):
#   a=str(input("name is: "))
#   hey()

# list1=[]
# def name(*):
"""import time
name = input("What is your name? ")
print("Hello" + name, "Time to play hangman!")
print(" ")
print("Start guessing...")
word = "sabo"
guesses = ''
turns = 10
while turns > 0:         
    failed = 0             
    for char in word:      
        if char in guesses:
          print (char),    
        else:
          print("_"),     
          failed += 1    
    if failed == 0:        
        print("You won")
        break              
    print()
    guess =input("guess a character:") 
    guesses += guess                    
    if guess not in word:  
      turns -= 1        
      print("Wrong")   
      print ("You have", + turns, 'more guesses' )
      if turns == 0:          
        print("You Lose")  """
