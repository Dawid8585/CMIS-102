from time import sleep

print("THE MORTAL COMBAT")

#input if its a new game
NewGame = input("is this a new game (Y/N)")
#if its a new game get the character issubclass
while NewGame == "Y" or NewGame == "y":
  Name = input("Enter Name of Character ")
  #is the characters name Uppercase or no
  SpellingName = Name.islower()
  if SpellingName == True:
    #if characters name isnt uppercase than make the first letter uppercase
    RealName = Name.title()
  Class = input("What are you? Are you a \n1: MAGE \n2: POKEMON  \n3: DEMON\n ")
  Level = 0;
  Inventory = list()
  break

#story!
print("\n*Dramatic Music playing*")
#allows time between print statements 
sleep(1)
print("\nDUN DUN DUUUUUNNNN dun duuuuun DDDDUUUUN DUUUUN")
sleep(6)
print("You wake up from a long nap in a clearing by the woods. No further than half a days walk from your village")
sleep(7)
print("\nIts a beautiful day out")
sleep(3)
print("\nIn the distance you hear a buzz ")
sleep(1)
print("............ ")
sleep(3)
choice = input("What do you do (Run , Hide, Attack)")

if choice == "Run" or choice == "RUN" or choice == "run":
  #counts how many letters in the name and uses it for distance user runs
  distances = len(Name)
  print("You run and run and only manage to go", distances,"feet before it catches you up.")
  sleep(2)
  print("\nturning around you see it and ")
  sleep(1)