mul3=0
mul35_list=[]
a=0
for i in range(1000):
    if (i%3==0 or i%5==0):
        mul35_list.append(i)
        mul3=mul3+i
for i in mul35_list:
    a=a+i

print(mul3)
print(mul35_list)
print(a)
        
