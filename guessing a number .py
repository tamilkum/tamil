from http.client import NO_CONTENT
import random 
number =random.randint(1,10)
player_name=input ("enter your name ")
no_of_guesses=1 
print(' hey '+player_name+ "guess a number between 1 and 10")
while no_of_guesses<=3:
    guess=int(input('guess'))
   
    if guess<number:
        print('guess is too low')
    if guess>number:
        print('guess is too high')
    if guess==number:
        print('you got it correct no . is: ',guess)
        break
    no_of_guesses+=1
if guess==number:
    print(" you guess the number "+str(no_of_guesses)+" trials")