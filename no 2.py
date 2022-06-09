age1=int(input("enter number"))
age2=int(input("enter number"))
age3=int(input("enter number"))
if age1>age2 and age3<age1:
    print("age1 is oldest")
elif age2>age3 and age1<age2:
    print("age2 is oldest")
elif age3>age1 and age2<age3:
    print("age3 is oldest")
if age1<age2 and age3>age1:
    print("age1 is youngest")
elif age2<age3 and age1>age2:
    print("age2 is youngest")
elif age3<age1 and age2>age3:
    print("age3 is yongest")
else:
    print("none")