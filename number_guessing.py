#the user will have to guess a number generated by the computer,the user will be given a certain number of chances to guess that number

#SKELETON:
#1)welcome message and game instruction
#2)show the user the difficulty levels
#3)ask them to choose the difficulty level
#4)start the game and see if their guess matches with the number generated by the computer
#5)if the user wins the game is over 
#6)else the user needs to guess within the guess limit otherwise he/she loses

import random   #to generate random numbers
import time    #for timer

computer=random.randint(1,100)  #computer will generate numbers between 1-100

chances=0  #initializing chances
attempts=0 #intializing attempts

#welcome message
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nYou'll have a few chances to guess the number depending on your difficulty level")
print("Please select the difficulty level: \n1)Easy(10 chances) \n2)Medium(5 chances) \n3)Hard(3 chance)")


while True: #the loop will run unless the user gives a valid input
    choice=int(input("Enter your choice: "))
    if choice==1:
        chances=10
        print (f"You chose 'Easy' difficulty level, you'll get {chances} chances")   
        break         
    elif choice==2:
        chances=5
        print (f"You chose 'Medium' difficulty level you'll get {chances} chances")  
        break       
    elif choice==3:
        chances=3
        print (f"You chose 'Hard' difficulty level, you'll get {chances} chance")
        break
    else:
        print("Invalid input.Choose from the given options")


print("Let's start the game")

start_time=time.time() #timer will start

while chances > 0: #the loop will run until chances are zero
    guess=int(input("Guess the number: "))
    attempts+=1

    if guess==computer:
        print(f"Congratulations!! You have won. You took {attempts} attempts to guess the number.")
        break
    elif guess<computer:
        chances-=1
        print(f"Wrong guess.The number is greater than {guess}.You have {chances} chances left")
    elif guess>computer:
        chances-=1
        print(f"Wrong guess.The number is  less than {guess}.You have {chances} chances left")


    if attempts==1 and guess==computer:
        print("Congratulations!! You have won on 1st attempt")

end_time=time.time() #timer will stop

time_taken=round(end_time-start_time,2) #it'll round up to 2 decimal place
print(f"You took {time_taken} seconds to guess the number.")

if chances==0:
        print("OOPSIE! You ran out of chances.")
        print(f"The number was {computer}")
        print(f"You took {time_taken} seconds.")