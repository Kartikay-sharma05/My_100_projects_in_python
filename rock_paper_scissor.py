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
print("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.")
user_choice = int(input())

computer_choice = random.randint(0,2)
if user_choice == 0:
  print(rock)
  if computer_choice == 0:
    print("Computer choose:")
    print(rock)
    print("Match draw")
  elif computer_choice == 1:
    print("Computer choose:")
    print(paper)
    print("Computer won")
  else:
    print("Computer choose:")
    print(scissors)
    print("You won")
elif user_choice == 1:
  print(paper)
  if computer_choice == 0:
    print("Computer choose:")
    print(rock)
    print("You won")
  elif computer_choice == 1:
    print("Computer choose:")
    print(paper)
    print("Match draw")
  else:
    print("Computer choose:")
    print(scissors)
    print("Computer won")
else:
  print(scissors)
  if computer_choice == 0:
    print("Computer choose:")
    print(rock)
    print("Computer won")
  elif computer_choice == 1:
    print("Computer choose:")
    print(paper)
    print("You won")
  else:
    print("Computer choose:")
    print(scissors)
    print("Match draw")