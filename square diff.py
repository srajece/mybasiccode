sqr_sum=0
sum_sqr=0
for i in range(101):
    sum_sqr=sum_sqr+(i*i)
    sqr_sum=(sqr_sum+i)
sqr_sum_total=sqr_sum*sqr_sum
    
print(sum_sqr)
print(sqr_sum_total)
result=sqr_sum_total-sum_sqr
print(result)
