a=int(input("enter a number:"))
series=[]
for i in range(1,a+1):
    series.append(2*i-1)
print("result",",".join(map(str,series)))