word='deeraj'
guesses = '' 
turns = 10
while turns > 0: 
    failed = 0
    for char in word:  
        if char in guesses:  
            print(char,end='')        
        else:  
            print("_ ",end='') 
            failed += 1
    if failed == 0: 
        print("You Win")  
        print("The word is: ", word)  
        break
    guess = input("\nguess a character:") 
    guesses += guess  
    if guess not in word: 
        turns -= 1
        print("Wrong") 
        print("You have", + turns, 'more guesses') 
        if turns == 0: 
            print("You Loose") 
'''
#
a='i am in chennai'
str1={}
for char in a:
    if char in str1:
        str1[char]+=1
    else:
        str1[char]=1
print(str1)
'''
