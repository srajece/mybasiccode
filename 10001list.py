
lis=[2]
count=0

for num in range(3,2000000,2):
   for i in range(3,num,2):
       if (num % i) == 0:
           break
   else:
       lis.append(num)
       if (num==10001):
          break
           
print(lis)
print(num)
