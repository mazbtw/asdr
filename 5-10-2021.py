for i in range(0,4):
    for j in range (1,5):
        if j==(i+1):
            print("N",end=" ")
        else:
            print(j,end=" ")
        if j%4==0:
            print()

while True:
    x=input("enter a nb or put Stop if u finish: ")
    if x=="Stop":
        break
    y=""
    for i in range(len(x)-1,-1,-1):
        y=y+x[i]
    if y==x:
        print("it is a palindrome.")
    else:
        print("it is not a palindrome.")
    