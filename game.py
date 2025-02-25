import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""


paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


rock_paper_scissors = [rock, paper, scissors]
player_choice = input(f'Choose 1,2 or 3 for Rock, Paper, or Scissors: ')

pick_random_rpc = random.choice(rock_paper_scissors)
if player_choice == "1":
    print(f'I choose Rock!\n{rock}')
    if pick_random_rpc == paper:
        print(f'I choose Paper!\n{paper}\nYou lose!')
    elif pick_random_rpc == scissors:
        print(f'I choose Scissors!\n{scissors}\nYou win!')
    elif pick_random_rpc == rock:
        print(f'I choose Rock!\n{rock}\nIt\'s a draw!')

elif player_choice == "2":
    print(f'I choose Paper!\n{paper}')
    if pick_random_rpc == paper:
        print(f'I choose Paper!\n{paper}\nIt\'s a draw!')
    elif pick_random_rpc == scissors:
        print(f'I choose Scissors!\n{scissors}\nYou lose!')
    elif pick_random_rpc == rock:
        print(f'I choose Rock!\n{rock}\nYou win!')
elif player_choice == "3":
    print(f'I choose Scissors!\n{scissors}')
    if pick_random_rpc == paper:
        print(f'I choose Paper!\n{paper}\nYou win!')
    elif pick_random_rpc == scissors:
        print(f'I choose Scissors!\n{scissors}\nIt\'s a draw!')
    elif pick_random_rpc == rock:
        print(f'I choose Rock!\n{rock}\nYou lose!')