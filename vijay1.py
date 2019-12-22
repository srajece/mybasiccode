with open("raj.txt") as fp:
   line = fp.readline()
   cnt = 1
   sep="offset="
   while line:
       text=line
       print(text)
       

       test=text[text.index(sep)+len(sep):]
       
       
       offset=test.split(" ")[0]
       print(offset)
       
       
         
       
       line = fp.readline()
       cnt += 1
       
       offset=float(offset)-50.5
       offset=str(offset)
       new_file=open('raj2.txt','a')
       new_file.write(text[:text.index(sep)+len(sep)]+offset+text[text.index(sep)+len(sep)+len(offset):])
       
       
       
fp.close()

