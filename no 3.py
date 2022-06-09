alphabet=input("enter alphabet") 
num=int(input("enter number"))
spl_cha=input("enter spl_cha")
a="a,b,c,d,e,f,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
b=1,2,3,4,5,6,7,8,9
c="!,@,#,$,%,*,&,^"
if alphabet in(a):
    print("alphabet=a")
elif num in(b):
    print("num=b")
elif spl_cha in(c):
    num=str(num)
    plus=alphabet+num+spl_cha
    print(plus,"password is strong")
else:
    print("none")
