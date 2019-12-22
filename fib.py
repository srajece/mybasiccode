a1,a2=0,1
b=[]


for i in range(0,1000):
    if a1+a2>=4000000:
        break
    b.append(i)
    
    b[i]=a1+a2
    a1=a2
    a2=b[i]
    
    
ans=0
for i in b:
    if (i%2==0):
        
        ans=ans+i

print (b)
print (ans)

    






















