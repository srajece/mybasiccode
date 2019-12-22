class TestFn:
    def __init__(self,name,age,totalmark):
         self.test_name=name
         self.test_age=age
         self.test_mark=totalmark
        
   

first_class=TestFn(name="anand",age="05", totalmark="80")
second_class=TestFn(name="bala",age="06", totalmark="65")
Third_class=TestFn(name="charlie",age="07", totalmark="90")

print(first_class.test_name)
