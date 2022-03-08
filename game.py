print('Number Guessing Game')
print('Guess the correct number from 1 to 9.You have 5 guesses with you.')
n=2
print('correct number is 2')
guess=0
while guess<5:
    g1=int(input('Enter Your Guess: '))
    if(g1>n):
        print('Not a correct guess. This was a much greater number.')
        guess+=1
    elif(g1==n):
        print('Correct Guess')
        break
    elif(g1<n):
        print('Not a correct guess. This was a much smaller number.')
        guess+=1
if(guess==5):
    print('You Loose.\nCorrect number was:',n)