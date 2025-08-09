import random

rock='''
 _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
paper ='''
 _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissor= '''
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
game_images=[rock,paper,scissor]

user_choice=int(input("""What do you choose?
Press 0 for ROCK.
Press 1 for PAPER.
Press 2 for SCISSOR.
Choose: """))
if user_choice>=0 and user_choice<=2:
    print(f"You chose: {user_choice}")
    print(game_images[user_choice])

computer_choice=random.randint(0,2)
print(f"Computer chose: {computer_choice}")
print(game_images[computer_choice])

if user_choice >=3 or user_choice<0:
    print("You chose an Invalid number. You Lose!")
elif user_choice==0 and computer_choice==2:
    print("You Win!")
elif computer_choice==0 and user_choice==2:
    print("You Lose!")
elif user_choice>computer_choice:
    print("You Win!")
elif computer_choice>user_choice:
    print("You Lose!")
elif computer_choice==user_choice:
    print("It's a Draw!")
    