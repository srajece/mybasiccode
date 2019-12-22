numbers=[2,4,6,8,3,2,6]
ans=[]
for i in numbers:
    if i not in ans:
        ans.append(i)
print(ans)
