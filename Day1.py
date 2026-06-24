Day 1        [18.6.2026]
1.Find greatest number 
a=int(input())
b=int(input())
c=int(input())

if a>b and a>c and a!=c and a!=b:
    print("a is greater")
    
elif b>c and b>a and b!=c and b!=a:
    print("b is greater")

elif a==b==c :
    print("all are equal")
    exit()
    
elif (a==b or b==c or a==c):
    if a==b :
        #print("a and b are equal")
        if a>c:
            print("a and b is equal and  greater than c")
        else:
            print("c is greater")
    if a==c:
        #print("a and c are equal")
        if a>b:
            print("a and c are equal and  greater b")
        else:
            print("b is greater")
    
    if b==c:
        #print("b and c are equal")
        if b>a:
            print("b and c are equal and  greater than a")
        else:
            print("a is greater")
    
elif c>a and c>b and c!=a and c!=b:
        print("c is greater")
else:
    exit()
    
2.Leap year or not
a=int(input())
if a%4==0:
    print("leap")
else:
    print("non")
    
3.star pattern
a=int(input())
for i in range (a+1):
    print("*"*i)








