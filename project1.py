#Roll the dies
import random
while True:
    choice=input("roll the dice? (y/n) 🎲: ").lower()
    if choice =="y":
         die1=random.randint(1,6)
         die2=random.randint(1,6)
         print(f"({die1},{die2})")
    elif choice =="n":
         print("thanks for playing!")     
         break
    else:
         print("invalid choice")

# Guess the number
import random
number_to_guess=random.randint(1,100)
print("Guess the number between 1 and 100 📲")
while True:
    try:
          guess=int(input("guess the number between 1 and 100: "))
          if guess<number_to_guess:
              print("too low!")
          elif guess>number_to_guess:
              print("too high!")    
          else:
             print("🎉🎉conguartulation! you guessed the number🎉🎉")
             break
    except ValueError:
       print("please enter a valid number")            

# rock,paper and scissor
import random
choices=("r","p","s")
user_choice=input("rock,paper,or scissors?(r/p/s): ").lower()
if user_choice not in choices:
    print("invalid choice")
computer_choice=random.choice(choices)  
print(f"you chose {user_choice}")  
print(f"computer chose {computer_choice}")
if user_choice==computer_choice:
    print("tie")
elif (user_choice=="r"and computer_choice=="s") or ( user_choice=="p" and computer_choice=="r") or (user_choice=="s"and computer_choice=="p"):
    print("🎉🎉 conguartulation you win the game🎉🎉")  
else:
    print("😔you lose the game😔")        