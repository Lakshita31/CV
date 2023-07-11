import random as r1
list1=[0,1,2]
c=r1.choice(list1)

name=input("Enter your name: ")
print("Welcome",name,"to Rock, Paper, Scissors game!")
u=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if c==0:
  print("Computer's choice is Rock")
elif c==1:
  print("Computer's choice is Paper")
else:
  print("Computer's choice is Scissors")
  
if u==0:
  print("Your choice is Rock")
elif u==1:
  print("Yours choice is Paper")
elif u==2:
  print("Your choice is Scissors")
else:
  print("Invalid input")


if u==0 and c==0:
  print("Your game is tie")
elif u==1 and c==0:
  print("You win")
elif u==2 and c==0:
  print("You loose")
elif u==0 and c==1:
  print("You loose")
elif u==1 and c==1:
  print("Your game is tie")
elif u==2 and c==1:
  print("You win ")
elif u==0 and c==2:
  print("You win")
elif u==1 and c==2:
  print("You loose")
elif u==2 and c==2:
  print("Your game is tie")
else:
  print("Invalid input!")