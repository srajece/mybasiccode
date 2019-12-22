class BaseClass(object):
    def __init__(self,water):
        print("Base")
        self.test_water=water
    
class TestFn(BaseClass):
    def __init__(self,name,age,totalmark,water_value):
        
        print("child")
        self.test_name=name
        self.test_age=age
        self.test_mark=totalmark
        super(TestFn,self).__init__(water_value)

    def display_name(self):
        print(self.test_name)
 
   

first_class=TestFn(name="anand",age="05", totalmark="80",water_value="watter")


print(first_class.test_water)
first_class.display_name()


