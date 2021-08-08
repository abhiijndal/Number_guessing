import random

n=random.randint(1,100)
x=None
guess=0
name=input('Enter your name:')
print('Hello!'+ ' '+str(name))

user=input('Do you wanna play number guessing game[Y/N]:')
if user=='y':
    print('Nice! So you have to guess the right number between 1 to 100 and')
    
    
    
    print('You have only 10 attempts to guess the right number ')
    
elif user=='n':
    print('oh! okay Have a nice day...')
    exit()



while n!=x:
    x=int(input('enter the guess:'))
    guess+=1
    if x>n:
        print('enter smaller number')
        
    elif x<n:
        print('enter the larger number')
        
    
    elif x==n:
        print('nice!your guess is right! game over')
    

    if guess>10:    
    
        print('-->wrong guess \U0001F910')
        print("*******************")
        print('==>Number is:'+str(n))
        print('*******************')
        print('-> you lose!')

        print("\U0001F612")
        exit()
   

if guess<=10:
    print('you won!')
    print("\N{smiling face with sunglasses}")
    


print(f'you guess the number in {guess} guesses \U0001F607')



  