rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

possibilities = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

computer_choice = random.randint(0, 2)

print(possibilities[choice])

print('Computer chose:')

print(possibilities[computer_choice])

if(choice == computer_choice):
  print("draw")
else:
  if((choice == 0 and computer_choice == 2) or (choice == 2 and computer_choice == 0)):
    if(computer_choice > choice):
      print("You won")
    else:
      print("You lose")
  else:
    if(choice > computer_choice):
      print("You won")
    else:
      print("You lose")