from collections import Counter

ini_list = [10, 20, 30, 20, 20, 30, 30, 33, 33, 33,
            5, 5, 5, 4, 4, 4, 4, 4, 4]

# printing initial ini_list 
print("initial list", str(ini_list))

# sorting on bais of frequency of elements 
result = sorted(ini_list, key=ini_list.count,
                reverse=True)

# printing final result 
print("final list", str(result))
