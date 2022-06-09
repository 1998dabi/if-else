clas=int(input("enter number"))
atten=int(input("enter number"))
percentage=clas/atten*100
if percentage>75:
    print("allow to sit",percentage)
else:
    print("not allow")