dic={'name':'python', 'address':{
    'city':'chennai','state':'TN',
    'street':{'value':{'test':'try','temp':'test_data'}}}}
                                 
key_list=['address','street','value','test']


def recursive_fn(dictionary,keys):
    if keys:
        print (dictionary)
        print(keys)
        print('*'*20)
        recursive_fn(dictionary[keys[0]],keys[1:])
    else:
        print(dictionary,'result')


recursive_fn(dic,key_list)    
