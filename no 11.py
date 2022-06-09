day=int(input("enter number"))
if day>=1 and day<=5:
    print("charge",day*2)
elif day>=6 and day<=10:
    print("charge",day*3)
elif day>=10 and day<=15:
    print("charge",day*4)
elif day>=15:
    print("charge",day*5)
else:
    print("none")