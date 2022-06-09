unit=int(input("enter number"))
quantity=unit*100
if quantity>=1000:
    discoun=quantity*10/100
    total=quantity-discoun
    print("total discoun",total)
else:
    print("none")