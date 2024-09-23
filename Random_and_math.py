import random
import math
#Floor
n1 = 7.5
floor = math.floor(n1)
print(f"Floor of {n1} is {floor}")
#Ceil
n2 = 7.5
ceil = math.ceil(n2)
print(f"Ceil of {n2} is {ceil}")
#isnan
n3 = float("nan")
print(f"Is 'nan' NaN: {math.isnan(n3)}")
playing = True
num = str(random.randint(0, 1))
print(len(str(100000000000000000000000000000000000000000000000000000000000)))
print("I have generated a random number between 0 and 10")
print("Guess the number")
while playing:
    guess = input("Enter your guess: ")
    if guess == num:
        print("You have guessed correctly.")
        break
    else:
        print("You have guessed wrong")
        print("Try again")
print("Enter choice: 'rock', 'paper' or 'scissors'")
player_choice = input("Choose move: ").lower()
options = ["rock", "paper", "scissors", "scissor"]
computer_choice = random.choice(options)
print(f"You chose {player_choice}")
print(f"The computer chose {computer_choice}")
if player_choice == computer_choice:
    print("It was a tie!")
elif player_choice == "rock" and computer_choice == "scissor" or computer_choice == "scissors":
    print("Rock crushes scissors. You win!")
elif player_choice == "paper" and computer_choice == "rock":
    print("Paper stops rocks (somehow). You win!")
elif player_choice == "scissor" or player_choice == "scissors" and computer_choice == "paper":
    print("Scissors cut paper. You win!")
else:
    print(f"{player_choice} does not beat {computer_choice}. You lose!")