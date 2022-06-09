quantity=int(input("enter number"))
cost=quantity*100
if cost>1000:
    discount=cost/100*10
    total_cost=cost-discount
    print("total_cost",total_cost)
else:
    print("none")