
lis=[2]
output=2


for num in range(3,200000,2):
   for i in range(3,num,2):
      if(num>10):
         if(num%3==0 or num%5==0 or num%7==0 or num%11==0 or num%13==0 or num%17==0 or num%19==0):
            break
      
      if (num % i) == 0:
         break
   else:
      print(num)
      output+=num
       
       
           
print(output)
print(num)
