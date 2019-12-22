first='raj'
last='kumar'
print(first + '[' +last+ '] is a trainer')
#print(f'{first} [{last}] is a decoder')
print('{0} {1} is a hacker'.format(first,last))



course='Python for Beginners'
if 'Python' in course:
    print(course.replace('Python','Cython'))




#find the letter in sentence
count=0
a=input("enter the string")
b=input("Enter the string to find in a")
for i in a:
    if (b==i):
        count=count+1
print(count)

#duplication del
numbers=[2,4,6,8,3,2,6]
ans=[]
for i in numbers:
    if i not in ans:
        ans.append(i)
print(ans)

#length
email="srajece@gmail.com"
countr =0
for i in email:
    countr=countr+1
    if i=="@":
        countr=countr-1
        print(countr)



