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

import random
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
comp_choice = random.randint(0, 2)
images = [rock, paper, scissors]

if choice > 2 or choice < 0:
  print("You entered an invalid number. You lose")
else:
  print(f"{images[choice]}")
  print(f"Computer chose: {images[comp_choice]}")
  if choice == comp_choice:
    print("Draw")
  elif choice == 0 and comp_choice == 2:
    print("You win")
  elif choice == 2 and comp_choice == 0:
    print("You lose")
  elif choice > comp_choice:
    print("You win")
  else:
    print("You lose")        
 