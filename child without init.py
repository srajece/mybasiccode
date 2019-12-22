class BaseClass():
    print('hai')
    def __init__(self,water):
        print("Base")
        self.test_water=water
    def get_water(self,bottle):
        print("getting hot {0} in {1}".format(self.test_water,bottle))
class TestFn(BaseClass):
    def get_water(self,bottle='office bottle'):
        self.bottle=bottle
        super(TestFn,self).get_water(self.bottle)
        print("Getting cold {0} from my class in {1}".format(self.test_water,bottle))
  
         
    def display_name(self):
        print(self.test_water)
   

#first_class=TestFn("water")
