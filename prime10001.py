
'''
count=0

for num in range(2,1000000000000000):
   for i in range(2,num):
       if (num % i) == 0:
           break
   else:
       count+=1
       print(count)
       if count==101:
           break
           
print(count)
print(num)
'''
