a=int(input("enter a number:"))
series=[]
if a%2 == 0:
    term = a-1
else:
    term =a
for i in range(1,term+1):
    series.append(2*i-1)
print("output",",".join(map(str,series)))
