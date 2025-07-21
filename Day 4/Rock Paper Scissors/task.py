#rules:
# Scissors wins against paper
# paper wins against rock
# rock wins against scissors


import random

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
list = ["Rock", "Scissors", "Paper"]
userChoice= int (input("What do you choose? rock = 0, paper = 1, scissors = 2"))
if random.choice(list) == list[0] and userChoice==0:
    print("Your choice is rock: ")
    print(rock)
    print("")
    print("Computer choice is rock: ")
    print(rock)
    print("")
    print("Its a draw!")
elif random.choice(list) == list[0] and userChoice == 1:
    print("Your choice is paper: ")
    print(paper)
    print("")
    print("Computer choice is rock: ")
    print(rock)
    print("")
    print("Paper beats rock, you win!")
elif random.choice(list) == list[0] and userChoice==2:
    print("Your choice is scissors: ")
    print(scissors)
    print("")
    print("Computer choice is rock: ")
    print(rock)
    print("")
    print("Rock beats scissors, you lose!")
elif random.choice(list) == list[1] and userChoice == 0:
    print("Your choice is rock: ")
    print(rock)
    print("")
    print("Computer choice is paper: ")
    print(paper)
    print("")
    print("Paper beats rock, you lose!")
elif random.choice(list) == list[1] and userChoice == 1:
    print("Your choice is paper: ")
    print(paper)
    print("")
    print("Computer choice is paper: ")
    print(paper)
    print("")
    print("Its a draw!")
elif random.choice(list) == list[1] and userChoice == 2:
    print("Your choice is scissors: ")
    print(scissors)
    print("")
    print("Computer choice is paper: ")
    print(paper)
    print("")
    print("Scissors beats paper, you win!")
elif random.choice(list) == list[2] and userChoice == 0:
    print("Your choice is rock: ")
    print(rock)
    print("")
    print("Computer choice is scissors: ")
    print(scissors)
    print("")
    print("Rock beats scissors, you win!")
elif random.choice(list) == list[2] and userChoice == 1:
    print("Your choice is paper: ")
    print(paper)
    print("")
    print("Computer choice is scissors: ")
    print(scissors)
    print("")
    print("Scissors beats paper, you lose!")
elif random.choice(list) == list[2] and userChoice == 2:
    print("Your choice is paper: ")
    print(scissors)
    print("")
    print("Computer choice is scissors: ")
    print(scissors)
    print("")
    print("Its a draw!")


