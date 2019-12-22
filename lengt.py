email="srajece@gmail.com"
countr =0
for i in email:
    countr=countr+1
    if i=="@":
        countr=countr-1
        print(countr)
