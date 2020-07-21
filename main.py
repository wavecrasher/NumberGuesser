import random

print("Welcome to Number Guesser")

#PROJECT PLAN W class
# - Computer Number# - Player number 
# - Tries
# - TriesOver
# - check player won

# - TypeError Handling

#global variable
comp_num = random.randint(0, 10)
tries = 3
won = False
play = True 

while play == True: 
  while tries > 0:
    print()
    player_num = input("Enter a number between 0-10: ")
    player_num = float(player_num)
    if player_num < 0 or player_num > 10: 
      print("Bad Number")
      break 
    else: 
      if player_num > comp_num:
        print("Number Too Big")
        tries -= 1
        print("You have" + str(tries) + "tries left")
      elif player_num < comp_num:
        print("Number too small")
        tries -= 1
        print ("You have" + str(tries) + "tries left")
      else:
        print("Correct")
        won = True
        break 
  if won == True:
    print ("Congratulations! You won at " + str(2-tries) + "tries")
  else: 
    print("No more tries")
    print("The number was: " + str(comp_num))
  answer = input("do you want to play again? Y/N ")
  if answer.upper() == "N":
    print("Ok then, byeee!")
    play == False 
  else:
    win = False 
    tries = 3
  comp_num = random.randint(0, 10)