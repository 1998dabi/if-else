unit=int(input("enter number"))
if unit>=1 and unit<=100:
    print("no charge")
elif unit>=100 and unit<=200:
    print("bill",unit*5)
elif unit>=200:
    a=unit-100
    b=5*100
    print("bill",a*10-b)
else:
    print("none")