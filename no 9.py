basic_salary=int(input("enter number"))
if basic_salary<=10000:
    HRA=basic_salary*20/100
    DA=basic_salary*80/100
    total=basic_salary+HRA+DA
    print("gross salary",total)
elif basic_salary<=20000:
    HRA=basic_salary*25/100
    DA=basic_salary*90/100
    total=basic_salary+HRA+DA
    print("gross salary",total)
elif basic_salary>20000:
    HRA=basic_salary*30/100
    DA=basic_salary*95/100
    total=basic_salary+HRA+DA
    print("gross salary",total)
else:
    print("none")

