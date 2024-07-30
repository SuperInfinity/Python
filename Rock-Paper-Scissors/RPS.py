import random as r

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
matrix = [[0, -1, 1],
          [1, 0, -1],
          [-1, 1, 0]]
choices = [rock, paper, scissors]
score = [0, 0]

print("Welcome to The Rock, Paper, Scissors Game!")
while True:
    key = True
    ch = input("Enter ur choice: (R/P/S): ").lower()
    if ch == 'r':
        ch = 0
    elif ch == 'p':
        ch = 1
    elif ch == 's':
        ch = 2
    else:
        print("Please enter valid choices..!")
        key = False
    
    if key:
        comp_ch = r.randint(0,2)
        print(f"Your choice\n{choices[ch]}\n")
        print(f"Computer's choice\n{choices[comp_ch]}\n")
        result = matrix[ch][comp_ch]
        if result == 0:
            print("That's a Tie..!")
        elif result == 1:
            score[1] += 1
            print("You Won..!")
            
        else:
            score[0] += 1
            print("You Lost..!")
        print(f"Scores now: \ncomp - {score[0]}\nYou - {score[1]}")