num=int(input("enter number"))
if num>=1500 and num<=2700:
    if num%7==0 and num%5==0:
        print("it is divisible")
    else:
        print("it is not divisible")
else:
    print("none")