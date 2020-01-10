word = 'bitaacademy'
comedy=['''






-------------------''','''
        |
        |
        |
        |
        |
        |
        |
-------------------''']

guess_count=10
a=["_" for i in range(len(word))]
def avalue(a):
    for i in a:
        print(i,end=' ')
    print('\n')
avalue(a)
while guess_count>=0:
    if guess_count==0:
        print('gameover')
        print('answer is',word)
        break
    if '_' not in a:
        print('you won')
        break
    print('total Chance',guess_count)
    guessletter=input('Enter the letter')
    if guessletter in a:
                print('its already entered')
                
    else:
        for i in range(len(word)):
            if guessletter in word:
                if word[i]==guessletter:
                    a[i]=word[i]
            else:
                guess_count-=1
                print(comedy[1])
                break
    avalue(a)

            
    



