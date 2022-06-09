year=int(input("enter number"))
if year%4==0:
    if year%100!=0 or year%400==0:
        print("it is leap year")
    else:
        print("none")
else:
    print("it is not leap year")