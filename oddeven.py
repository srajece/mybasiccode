even_list=[]
odd_list=[]
for i in range(1,101):
    if(i%2==0):
        even_list.append(i)
    if(i%2!=0):
        odd_list.append(i)
print(odd_list)
print(even_list)
